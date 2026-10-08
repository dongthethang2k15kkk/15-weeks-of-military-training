from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

SEED = 2026

# ---------------------------------------------------------------- tham số chuyến xe
T_TONG = 180.0                    # giây
DT = 0.005                        # bước mô phỏng (200 Hz), chia hết cho 50 Hz, 20 Hz, 1 Hz
GIO_BAT_DAU_UTC = (16, 59, 0)     # 23:59:00 giờ Việt Nam
NGAY_UTC = "081026"               # ddmmyy, dùng trong câu RMC
LAT0, LON0 = 21.0045, 105.8430    # điểm xuất phát, khuôn viên ĐHBK Hà Nội
MET_MOT_DO_VI_DO = 111320.0

# Vật cản và phanh gấp
T_VAT_CAN_XUAT_HIEN = 112.8       # s, vật cản chen vào cách xe 9.0 m
KC_VAT_CAN_LUC_XUAT_HIEN = 9.0    # m
T_PHANH = 113.1                   # s, bắt đầu phanh gấp
GIA_TOC_PHANH = 7.0               # m/s^2
T_DUNG = T_PHANH + (30 / 3.6) / GIA_TOC_PHANH
T_VAT_CAN_DI = 135.0              # s, vật cản bắt đầu rời đi
GIA_TOC_VAT_CAN_DI = 2.0          # m/s^2

# Điểm gãy của profile tốc độ: (giây, km/h)
DIEM_TOC_DO = [
    (0, 0), (15, 0), (35, 40), (60, 40), (80, 65), (92, 35), (100, 30),
    (T_PHANH, 30), (T_DUNG, 0), (136, 0), (148, 27), (T_TONG, 27),
]

# Hai lần rẽ: (giây bắt đầu, thời lượng, góc quay ngược chiều kim đồng hồ, độ)
LAN_RE = [(42.0, 10.0, +90.0), (91.0, 8.0, -90.0)]

# Pin: 15.8% lúc đầu, giảm đều theo quãng đường, qua mốc 14.95% (hiển thị 14.9) ở t = 164.5 s.
# Tốc độ tụt pin đã được nén cho vừa chuyến 3 phút.
PIN_BAT_DAU = 15.8
T_PIN_QUA_MOC = 164.5

# Cảm biến
TAM_TOI_DA_CM = 1200.0
TAM_TOI_THIEU_CM = 10.0
NHIEU_LIDAR_CM = 2.0
NHIEU_GIA_TOC = 0.05              # m/s^2
NHIEU_CON_QUAY = 0.1              # độ/giây
TI_LE_MAT_TIN_HIEU = 0.01
SO_DONG_TRONG = 8
KNOT_TREN_MS = 1.943844

# Mã fix GPS theo thời gian (giây, mã). Mất fix 3 s quanh t = 95.
DOAN_FIX = [(0, 1), (6, 2), (35, 5), (48, 4), (93.5, 0), (96.5, 5), (106, 4)]
SAI_SO_VI_TRI_M = {0: 0.0, 1: 2.5, 2: 0.8, 4: 0.02, 5: 0.25}
SO_VE_TINH = {0: 0, 1: 7, 2: 11, 4: 18, 5: 16}
HDOP = {0: None, 1: 1.4, 2: 1.0, 4: 0.6, 5: 0.8}
SAI_SO_DO_CAO_M = {0: 0.0, 1: 1.0, 2: 0.5, 4: 0.05, 5: 0.2}
CHE_DO_RMC = {1: "A", 2: "D", 4: "R", 5: "F"}


# ---------------------------------------------------------------- mô phỏng vật lý
def tich_phan(y: np.ndarray) -> np.ndarray:
    """Tích phân hình thang theo DT, bắt đầu từ 0."""
    return np.concatenate([[0.0], np.cumsum((y[1:] + y[:-1]) / 2 * DT)])


def mo_phong() -> dict:
    n = round(T_TONG / DT)
    t = np.arange(n + 1) * DT

    cot_t, cot_v = zip(*DIEM_TOC_DO)
    v_tho = np.interp(t, cot_t, np.array(cot_v) / 3.6)
    cua_so = 100                                    # 0.5 s, làm mượt các góc gãy
    v = np.convolve(np.pad(v_tho, (cua_so // 2, cua_so // 2 - 1), mode="edge"),
                    np.ones(cua_so) / cua_so, mode="valid")
    a = np.gradient(v, DT)
    s = tich_phan(v)

    omega_do = np.zeros_like(t)                     # độ/giây, dương = rẽ trái
    for bat_dau, thoi_luong, goc in LAN_RE:
        tau = t - bat_dau
        trong = (tau >= 0) & (tau <= thoi_luong)
        omega_do[trong] = goc / thoi_luong * (1 - np.cos(2 * np.pi * tau[trong] / thoi_luong))
    huong = -np.deg2rad(tich_phan(omega_do))        # rad, tính theo chiều kim đồng hồ từ hướng Bắc
    x = tich_phan(v * np.sin(huong))                # mét về phía Đông
    y = tich_phan(v * np.cos(huong))                # mét về phía Bắc

    i_xuat_hien = round(T_VAT_CAN_XUAT_HIEN / DT)
    s_vat_can = s[i_xuat_hien] + KC_VAT_CAN_LUC_XUAT_HIEN
    s_vc = np.full_like(t, s_vat_can)
    di = t > T_VAT_CAN_DI
    s_vc[di] += 0.5 * GIA_TOC_VAT_CAN_DI * (t[di] - T_VAT_CAN_DI) ** 2
    khoang_cach = np.where(t >= T_VAT_CAN_XUAT_HIEN, s_vc - s, np.inf)
    khoang_cach[khoang_cach > TAM_TOI_DA_CM / 100] = np.inf

    he_so_pin = (PIN_BAT_DAU - 14.95) / s[round(T_PIN_QUA_MOC / DT)]
    pin = PIN_BAT_DAU - he_so_pin * s

    return dict(t=t, v=v, a=a, s=s, omega_do=omega_do, huong=huong, x=x, y=y,
                khoang_cach=khoang_cach, pin=pin)


def ma_fix(t_giay: float) -> int:
    ma = DOAN_FIX[0][1]
    for moc, gia_tri in DOAN_FIX:
        if t_giay >= moc:
            ma = gia_tri
    return ma


# ---------------------------------------------------------------- sinh từng file
def sinh_khoang_cach(mp: dict, rs: np.random.RandomState) -> list[str]:
    buoc = round(0.05 / DT)
    t, kc = mp["t"][::buoc], mp["khoang_cach"][::buoc]
    nhieu = rs.normal(0.0, NHIEU_LIDAR_CM, size=len(t))
    cm = np.where(np.isinf(kc), TAM_TOI_DA_CM,
                  np.clip(kc * 100 + nhieu, TAM_TOI_THIEU_CM, TAM_TOI_DA_CM))
    chi_so = rs.choice(len(t), size=round(len(t) * TI_LE_MAT_TIN_HIEU) + SO_DONG_TRONG,
                       replace=False)
    mat_tin_hieu = set(chi_so[: len(chi_so) - SO_DONG_TRONG].tolist())
    dong_trong = set(chi_so[len(chi_so) - SO_DONG_TRONG:].tolist())

    dong = ["thoi_gian_s,khoang_cach_cm"]
    for i, (ti, ci) in enumerate(zip(t, cm)):
        if i in mat_tin_hieu:
            dong.append(f"{ti:.2f},0.0")
        elif i in dong_trong:
            dong.append(f"{ti:.2f},")
        else:
            dong.append(f"{ti:.2f},{ci:.1f}")
    return dong


def sinh_imu(mp: dict, rs: np.random.RandomState) -> list[str]:
    buoc = round(0.02 / DT)
    sl = slice(None, None, buoc)
    t, a, v, om = mp["t"][sl], mp["a"][sl], mp["v"][sl], mp["omega_do"][sl]
    n = len(t)
    ax = a + rs.normal(0, NHIEU_GIA_TOC, n)
    ay = v * np.deg2rad(om) + rs.normal(0, NHIEU_GIA_TOC, n)
    az = 9.81 + rs.normal(0, NHIEU_GIA_TOC, n)
    gx = rs.normal(0, NHIEU_CON_QUAY, n)
    gy = rs.normal(0, NHIEU_CON_QUAY, n)
    gz = om + rs.normal(0, NHIEU_CON_QUAY, n)

    dong = ["thoi_gian_s,ax,ay,az,gx,gy,gz"]
    for i in range(n):
        dong.append(f"{t[i]:.2f},{ax[i]:.3f},{ay[i]:.3f},{az[i]:.3f},"
                    f"{gx[i]:.2f},{gy[i]:.2f},{gz[i]:.2f}")
    return dong


def sinh_obd(mp: dict, rs: np.random.RandomState) -> list[str]:
    buoc = round(1.0 / DT)
    sl = slice(None, None, buoc)
    t, v, a, pin = mp["t"][sl], mp["v"][sl], mp["a"][sl], mp["pin"][sl]
    kmh = np.rint(v * 3.6).astype(int)
    rpm = np.rint(800 + 35 * v * 3.6 + 40 * np.maximum(a, 0)
                  + rs.normal(0, 12, len(t))).astype(int)
    dong = ["thoi_gian_s,toc_do_kmh,rpm,muc_pin_pct"]
    for i in range(len(t)):
        dong.append(f"{t[i]:.2f},{kmh[i]},{rpm[i]},{pin[i]:.1f}")
    return dong


def checksum_nmea(noi_dung: str) -> str:
    """XOR các ký tự nằm giữa '$' và '*'."""
    kq = 0
    for ky_tu in noi_dung:
        kq ^= ord(ky_tu)
    return f"{kq:02X}"


def cau_nmea(noi_dung: str) -> str:
    return f"${noi_dung}*{checksum_nmea(noi_dung)}"


def toa_do_nmea(do_thap_phan: float, so_chu_so_do: int) -> str:
    """Độ thập phân -> ddmm.mmmmm (vĩ độ) hoặc dddmm.mmmmm (kinh độ)."""
    do = int(do_thap_phan)
    phut_nghin = round((do_thap_phan - do) * 60 * 1e5)
    if phut_nghin >= 60 * 100000:
        do, phut_nghin = do + 1, phut_nghin - 60 * 100000
    return f"{do:0{so_chu_so_do}d}{phut_nghin // 100000:02d}.{phut_nghin % 100000:05d}"


def sinh_gps(mp: dict, rs: np.random.RandomState) -> list[str]:
    buoc = round(1.0 / DT)
    chi_so = np.arange(0, len(mp["t"]), buoc)
    so_mau = len(chi_so)
    nhieu = rs.normal(0, 1, size=(so_mau, 2))
    nhieu_cao = rs.normal(0, 1, size=so_mau)

    dong = []
    for k, i in enumerate(chi_so):
        giay = k
        h, m, s0 = GIO_BAT_DAU_UTC
        tong = h * 3600 + m * 60 + s0 + giay
        gio = f"{tong // 3600 % 24:02d}{tong // 60 % 60:02d}{tong % 60:02d}.00"
        fix = ma_fix(giay)
        v = mp["v"][i]
        if fix == 0:
            dong.append(cau_nmea(f"GNRMC,{gio},V,,,,,,,{NGAY_UTC},,,N"))
            dong.append(cau_nmea(f"GNGGA,{gio},,,,,0,00,,,,,,,"))
            continue

        sai_so = SAI_SO_VI_TRI_M[fix]
        dong_m = mp["x"][i] + nhieu[k, 0] * sai_so
        bac_m = mp["y"][i] + nhieu[k, 1] * sai_so
        vi_do = LAT0 + bac_m / MET_MOT_DO_VI_DO
        kinh_do = LON0 + dong_m / (MET_MOT_DO_VI_DO * np.cos(np.deg2rad(LAT0)))
        lat, lon = toa_do_nmea(vi_do, 2), toa_do_nmea(kinh_do, 3)
        huong_do = f"{np.rad2deg(mp['huong'][i]) % 360:.1f}" if v > 0.5 else ""
        dong.append(cau_nmea(
            f"GNRMC,{gio},A,{lat},N,{lon},E,{v * KNOT_TREN_MS:.2f},{huong_do},"
            f"{NGAY_UTC},,,{CHE_DO_RMC[fix]}"))
        do_cao = 12.3 + nhieu_cao[k] * SAI_SO_DO_CAO_M[fix]
        tuoi_dc = "1.0" if fix in (2, 4, 5) else ""
        tram_dc = "0000" if fix in (2, 4, 5) else ""
        dong.append(cau_nmea(
            f"GNGGA,{gio},{lat},N,{lon},E,{fix},{SO_VE_TINH[fix]:02d},{HDOP[fix]},"
            f"{do_cao:.1f},M,-22.1,M,{tuoi_dc},{tram_dc}"))
    return dong


# ---------------------------------------------------------------- ghi file, kiểm tra
def ghi_file(duong_dan: Path, dong: list[str]) -> None:
    with open(duong_dan, "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(dong) + "\n")


def in_su_kien(mp: dict) -> None:
    t, v, a = mp["t"], mp["v"] * 3.6, mp["a"]
    kc = mp["khoang_cach"]

    def lan_dau(dieu_kien):
        i = np.argmax(dieu_kien)
        return f"{t[i]:.2f} s" if dieu_kien[i] else "khong co"

    print("Doi chieu bang su kien (muc 5.1):")
    print(f"  toc do lon nhat           : {v.max():.1f} km/h, vuot 60 luc {lan_dau(v > 60)}")
    print(f"  ax nho nhat               : {a.min():.2f} m/s^2, lan dau < -5 luc {lan_dau(a < -5)}")
    print(f"  xe dung han luc           : {lan_dau((t > T_PHANH) & (v < 0.05))}")
    print(f"  vat can xuat hien         : {lan_dau(np.isfinite(kc))}, "
          f"khoang cach dau tien {kc[np.isfinite(kc)][0]:.2f} m")
    dung = (t > T_DUNG + 1) & (t < T_VAT_CAN_DI)
    print(f"  khoang cach luc xe dung   : {kc[dung].min():.2f} - {kc[dung].max():.2f} m")
    print(f"  khoang cach <= 2.0 luc    : {lan_dau(kc <= 2.0)}")
    print(f"  pin < 15 (hien thi 14.9)  : {lan_dau(mp['pin'] < 14.95)}, cuoi chuyen {mp['pin'][-1]:.2f}%")
    print(f"  quang duong ca chuyen     : {mp['s'][-1]:.0f} m")
    cac_fix = [(giay, ma_fix(giay)) for giay in range(int(T_TONG) + 1)]
    doi = [cac_fix[0]] + [c for p, c in zip(cac_fix, cac_fix[1:]) if p[1] != c[1]]
    print("  ma fix GPS (giay: ma)     :", ", ".join(f"{g}:{m}" for g, m in doi))


def ve_kiem_tra(mp: dict, duong_dan: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    t = mp["t"]
    kc = np.where(np.isinf(mp["khoang_cach"]), np.nan, mp["khoang_cach"])
    fig, ax = plt.subplots(2, 2, figsize=(13, 8))
    ax[0, 0].plot(t, mp["v"] * 3.6)
    ax[0, 0].axhline(60, color="gray", ls="--")
    ax[0, 0].set(title="Toc do (km/h)", xlabel="t (s)")
    ax[0, 1].plot(t, kc)
    ax[0, 1].axhline(2.0, color="red", ls="--")
    ax[0, 1].axhline(5.0, color="orange", ls="--")
    ax[0, 1].set(title="Khoang cach toi vat can (m), trong = tam toi da", xlabel="t (s)")
    ax[1, 0].plot(t, mp["a"])
    ax[1, 0].axhline(-5, color="red", ls="--")
    ax[1, 0].set(title="ax = gia toc doc (m/s^2)", xlabel="t (s)")
    mau = {0: "black", 1: "gray", 2: "tab:blue", 5: "tab:orange", 4: "tab:green"}
    for giay in range(int(T_TONG) + 1):
        i = round(giay / DT)
        fix = ma_fix(giay)
        if fix:
            ax[1, 1].scatter(mp["x"][i], mp["y"][i], c=mau[fix], s=8)
    ax[1, 1].set(title="Quy dao GPS (xanh la = RTK fixed)", xlabel="Dong (m)", ylabel="Bac (m)")
    ax[1, 1].set_aspect("equal")
    fig.tight_layout()
    fig.savefig(duong_dan, dpi=110)
    print("Da luu hinh kiem tra:", duong_dan)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ve", metavar="FILE.png", help="ghi hình kiểm tra 4 ô")
    ap.add_argument("--ra", default=None, help="thư mục ghi (mặc định: data/ của repo)")
    args = ap.parse_args()

    thu_muc = Path(args.ra) if args.ra else Path(__file__).resolve().parent.parent / "data"
    thu_muc.mkdir(parents=True, exist_ok=True)

    rs = np.random.RandomState(SEED)
    mp = mo_phong()
    ghi_file(thu_muc / "khoang_cach_truoc.csv", sinh_khoang_cach(mp, rs))
    ghi_file(thu_muc / "imu.csv", sinh_imu(mp, rs))
    ghi_file(thu_muc / "obd.csv", sinh_obd(mp, rs))
    ghi_file(thu_muc / "gps.nmea", sinh_gps(mp, rs))

    for ten in ("khoang_cach_truoc.csv", "gps.nmea", "obd.csv", "imu.csv"):
        p = thu_muc / ten
        so_dong = sum(1 for _ in open(p, "rb"))
        print(f"  {ten:24s} {so_dong:6d} dong  {p.stat().st_size / 1024:7.1f} KB")
    in_su_kien(mp)
    if args.ve:
        ve_kiem_tra(mp, args.ve)


if __name__ == "__main__":
    main()
