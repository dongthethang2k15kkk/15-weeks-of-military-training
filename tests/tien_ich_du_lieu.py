"""Hàm đọc, đồng bộ và vẽ dữ liệu chuyến xe, viết sẵn cho học viên dùng.

  - doc_chuyen_xe(): đọc các file trong data/, đồng bộ về 1 Hz.
  - ve_chuyen_xe(ham_quyet_dinh): vẽ kết quả của một hàm quyết định lên chuyến xe.
"""

from __future__ import annotations

import csv
import math
import statistics
from pathlib import Path

TAM_TOI_DA_M = 12.0
MAU_THEO_LENH = {
    "DUNG_KHAN_CAP": "red",
    "VE_TRAM_SAC": "orange",
    "GIAM_TOC": "gold",
    "BINH_THUONG": "green",
}


def duong_dan_data(ten_file: str) -> Path:
    """Tìm file trong data/, chạy được ở Colab (thư mục làm việc) và trên GitHub Actions."""
    goc_tests = Path(__file__).resolve().parent.parent
    for thu_muc in (Path.cwd() / "data", Path.cwd().parent / "data", goc_tests / "data"):
        duong_dan = thu_muc / ten_file
        if duong_dan.is_file():
            return duong_dan
    raise FileNotFoundError(f"Không tìm thấy data/{ten_file}. Chạy lại ô thiết lập ở đầu notebook.")


def _khoang_cach_theo_giay() -> dict[int, list[float]]:
    """Gom các mẫu LiDAR hợp lệ (mét) theo từng giây, bỏ dòng ô trống và dòng 0.0."""
    cac_mau: dict[int, list[float]] = {}
    with open(duong_dan_data("khoang_cach_truoc.csv"), encoding="utf-8") as f:
        next(f)
        for dong in f:
            thoi_gian, _, o_khoang_cach = dong.strip().partition(",")
            if o_khoang_cach == "" or float(o_khoang_cach) == 0.0:
                continue
            cac_mau.setdefault(int(float(thoi_gian)), []).append(float(o_khoang_cach) / 100)
    return cac_mau


def doc_chuyen_xe():
    """Mỗi lần lặp trả về (t, khoang_cach_m, toc_do_kmh, muc_pin_pct) của một giây.

    khoang_cach_m là trung vị các mẫu LiDAR hợp lệ trong giây đó, None nếu không có mẫu nào.
    """
    cac_mau = _khoang_cach_theo_giay()
    with open(duong_dan_data("obd.csv"), encoding="utf-8") as f:
        for hang in csv.DictReader(f):
            t = int(float(hang["thoi_gian_s"]))
            mau_giay = cac_mau.get(t)
            khoang_cach = statistics.median(mau_giay) if mau_giay else None
            yield t, khoang_cach, int(hang["toc_do_kmh"]), float(hang["muc_pin_pct"])


def _nmea_sang_do(chuoi: str) -> float:
    x = float(chuoi)
    return x // 100 + (x % 100) / 60


def _quy_dao_gps() -> dict[int, tuple[float, float]]:
    """Giây thứ k -> (đông, bắc) tính bằng mét so với điểm xuất phát. Bỏ giây mất fix."""
    diem: dict[int, tuple[float, float]] = {}
    goc = None
    giay = -1
    with open(duong_dan_data("gps.nmea"), encoding="utf-8") as f:
        for dong in f:
            if not dong.startswith("$GNGGA"):
                continue
            giay += 1
            cot = dong.split(",")
            if cot[2] == "" or cot[4] == "":
                continue
            vi_do, kinh_do = _nmea_sang_do(cot[2]), _nmea_sang_do(cot[4])
            if goc is None:
                goc = (vi_do, kinh_do)
            bac = (vi_do - goc[0]) * 111320.0
            dong_m = (kinh_do - goc[1]) * 111320.0 * math.cos(math.radians(goc[0]))
            diem[giay] = (dong_m, bac)
    return diem


def ve_chuyen_xe(ham_quyet_dinh) -> None:
    """Vẽ hai hình cạnh nhau, màu theo lệnh mà ham_quyet_dinh(khoang_cach, toc_do, muc_pin) trả về.

    Trái: tốc độ và khoảng cách theo thời gian. Phải: quỹ đạo GPS.
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    ban_ghi = list(doc_chuyen_xe())
    lenh = [None if kc is None else ham_quyet_dinh(kc, v, pin) for _, kc, v, pin in ban_ghi]
    if all(l is None for l in lenh):
        print("Xong hàm quyết định rồi chạy lại ô này để xem hình.")
        return

    fig, (hinh_trai, hinh_phai) = plt.subplots(1, 2, figsize=(14, 5))

    for (t, _, _, _), l in zip(ban_ghi, lenh):
        hinh_trai.axvspan(t, t + 1, color=MAU_THEO_LENH.get(l, "lightgray"), alpha=0.3, linewidth=0)
    thoi_gian = [b[0] for b in ban_ghi]
    hinh_trai.plot(thoi_gian, [b[2] for b in ban_ghi], color="tab:blue")
    hinh_trai.set_xlabel("Thời gian (s)")
    hinh_trai.set_ylabel("Tốc độ (km/h)", color="tab:blue")
    truc_kc = hinh_trai.twinx()
    truc_kc.plot(thoi_gian, [float("nan") if b[1] is None else b[1] for b in ban_ghi],
                 color="black", linewidth=1)
    truc_kc.set_ylabel("Khoảng cách phía trước (m)")
    truc_kc.set_ylim(0, TAM_TOI_DA_M + 1)
    hinh_trai.set_title("Tốc độ và khoảng cách, nền tô màu theo lệnh")

    quy_dao = _quy_dao_gps()
    for (t, _, _, _), l in zip(ban_ghi, lenh):
        if t in quy_dao:
            uu_tien = list(MAU_THEO_LENH).index(l) if l in MAU_THEO_LENH else len(MAU_THEO_LENH)
            hinh_phai.scatter(*quy_dao[t], color=MAU_THEO_LENH.get(l, "lightgray"), s=25,
                              zorder=len(MAU_THEO_LENH) - uu_tien)    # lệnh nghiêm trọng vẽ lên trên
    hinh_phai.set_xlabel("Hướng Đông (m)")
    hinh_phai.set_ylabel("Hướng Bắc (m)")
    hinh_phai.set_aspect("equal")
    hinh_phai.set_title("Quỹ đạo GPS theo lệnh")
    hinh_phai.legend(handles=[Patch(color=m, label=ten) for ten, m in MAU_THEO_LENH.items()],
                     loc="lower left", fontsize=8)

    fig.tight_layout()
    plt.show()
