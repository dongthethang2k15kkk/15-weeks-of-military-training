"""Bộ test tuần 1 - Nền tảng & Cú pháp cơ bản.

Tuần 1 chấm theo hai kiểu, tuỳ bài đã dạy tới đâu:

  - Bài 1 đến Bài 3 chưa có `def`, nên các hàm kiem_tra_* nhận thẳng GIÁ TRỊ biến
    học viên đã gán. Gọi ví dụ: kiem_tra_1_1(tb_doc_1, tb_doc_2)
  - Bài 4 và Dự án đã dạy `def`, nên nhận HÀM và tự chọn đầu vào để gọi.
    Gọi ví dụ: kiem_tra_4_1(canh_bao_vat_can)
"""

from __future__ import annotations

try:
    from .runner import Case, kiem_tra, kiem_tra_gia_tri
except ImportError:  # khi chạy trực tiếp trong Colab, không qua package
    from runner import Case, kiem_tra, kiem_tra_gia_tri


# --------------------------------------------------------------------------
# Bài 1: Biến và kiểu dữ liệu
# --------------------------------------------------------------------------

def kiem_tra_1_1(tb_doc_1, tb_doc_2) -> bool:
    """tb_doc_1, tb_doc_2 -> trung bình cộng ba lần đọc cảm biến, không làm tròn."""
    return kiem_tra_gia_tri(
        "Bài 1.1 - Trung bình lần đọc cảm biến",
        [
            ("tb_doc_1 (cảm biến 1: 8, 9, 10)", tb_doc_1, (8 + 9 + 10) / 3),
            ("tb_doc_2 (cảm biến 2: 7.5, 6, 8)", tb_doc_2, (7.5 + 6 + 8) / 3),
        ],
    )


def kiem_tra_1_2(noi_chuoi, tong_so) -> bool:
    """noi_chuoi -> nối chuỗi "20" với "5". tong_so -> ép "20" sang số rồi +5."""
    return kiem_tra_gia_tri(
        "Bài 1.2 - Ép kiểu dữ liệu",
        [
            ("noi_chuoi (gia_tri_tho_2 + \"5\")", noi_chuoi, "205"),
            ("tong_so (int(gia_tri_tho_2) + 5)", tong_so, 25),
        ],
    )


# --------------------------------------------------------------------------
# Bài 2: Toán tử, chuỗi và ép kiểu
# --------------------------------------------------------------------------

def kiem_tra_2_1(moi_xe_tra_1, moi_xe_tra_2) -> bool:
    """moi_xe_tra_1, moi_xe_tra_2 -> tiền mỗi xe sau phí dịch vụ, làm tròn 2 chữ số."""
    return kiem_tra_gia_tri(
        "Bài 2.1 - Chia tiền sạc",
        [
            ("moi_xe_tra_1 (300000, phí dv 10%, 3 xe)", moi_xe_tra_1, 110000.0),
            ("moi_xe_tra_2 (100000, phí dv 15%, 3 xe)", moi_xe_tra_2, 38333.33),
        ],
    )


def kiem_tra_2_2(bao_cao) -> bool:
    """bao_cao -> chuỗi f-string đúng mẫu, quãng đường = 20.0 * 3."""
    return kiem_tra_gia_tri(
        "Bài 2.2 - Báo cáo quãng đường",
        [
            ("bao_cao", bao_cao, "Xe đã đi được 60.0 mét trong 3 giây."),
        ],
    )


def kiem_tra_2_3(gio, phut, giay) -> bool:
    """gio, phut, giay -> đổi 5000 giây bằng // và %."""
    return kiem_tra_gia_tri(
        "Bài 2.3 - Đổi giây sang giờ phút giây",
        [
            ("gio (5000 giây)", gio, 1),
            ("phut (5000 giây)", phut, 23),
            ("giay (5000 giây)", giay, 20),
        ],
    )


# --------------------------------------------------------------------------
# Bài 3: Boolean và câu lệnh điều kiện - chấm theo giá trị, mỗi bài một trường hợp
# --------------------------------------------------------------------------

def kiem_tra_3_1(trang_thai) -> bool:
    """trang_thai -> phân loại khoang_cach = 3.7 theo bảng ngưỡng."""
    return kiem_tra_gia_tri(
        "Bài 3.1 - Cảnh báo vật cản",
        [
            ("trang_thai (khoang_cach = 3.7)", trang_thai, "GIAM_TOC"),
        ],
    )


def kiem_tra_3_2(gioi_han) -> bool:
    """gioi_han -> tốc độ cho phép trên duong_tinh khi trời mưa."""
    return kiem_tra_gia_tri(
        "Bài 3.2 - Giới hạn tốc độ",
        [
            ('gioi_han (loai_duong = "duong_tinh", troi_mua = True)', gioi_han, 60),
        ],
    )


# --------------------------------------------------------------------------
# Bài 4: Hàm - chấm bằng cách gọi hàm với đầu vào do bộ chấm chọn
# --------------------------------------------------------------------------

def kiem_tra_4_1(canh_bao_vat_can) -> bool:
    """canh_bao_vat_can(khoang_cach) -> chuỗi cảnh báo, kiểm cả giá trị biên."""
    return kiem_tra(
        "Bài 4.1 - Hàm cảnh báo vật cản",
        canh_bao_vat_can,
        [
            Case(args=(0.5,), expected="PHANH_KHAN_CAP", mo_ta="canh_bao_vat_can(0.5)"),
            Case(args=(2.0,), expected="PHANH_KHAN_CAP", mo_ta="canh_bao_vat_can(2.0) - biên dưới"),
            Case(args=(3.7,), expected="GIAM_TOC", mo_ta="canh_bao_vat_can(3.7)"),
            Case(args=(5.0,), expected="GIAM_TOC", mo_ta="canh_bao_vat_can(5.0) - biên trên"),
            Case(args=(12.0,), expected="AN_TOAN", mo_ta="canh_bao_vat_can(12.0)"),
        ],
    )


def kiem_tra_4_2(gioi_han_toc_do) -> bool:
    """gioi_han_toc_do(loai_duong, troi_mua) -> giới hạn km/h theo bảng hai chiều."""
    return kiem_tra(
        "Bài 4.2 - Hàm giới hạn tốc độ",
        gioi_han_toc_do,
        [
            Case(args=("khu_truong_hoc", False), expected=30,
                 mo_ta='gioi_han_toc_do("khu_truong_hoc", False)'),
            Case(args=("khu_truong_hoc", True), expected=30,
                 mo_ta='gioi_han_toc_do("khu_truong_hoc", True) - mưa không đổi'),
            Case(args=("khu_dan_cu", False), expected=50,
                 mo_ta='gioi_han_toc_do("khu_dan_cu", False)'),
            Case(args=("khu_dan_cu", True), expected=40,
                 mo_ta='gioi_han_toc_do("khu_dan_cu", True)'),
            Case(args=("duong_tinh", True), expected=60,
                 mo_ta='gioi_han_toc_do("duong_tinh", True)'),
            Case(args=("cao_toc", False), expected=120,
                 mo_ta='gioi_han_toc_do("cao_toc", False)'),
            Case(args=("cao_toc", True), expected=90,
                 mo_ta='gioi_han_toc_do("cao_toc", True)'),
        ],
    )


# --------------------------------------------------------------------------
# Dự án tuần 1
# --------------------------------------------------------------------------

def kiem_tra_du_an(quyet_dinh_lai_xe) -> bool:
    """quyet_dinh_lai_xe(khoang_cach, toc_do, muc_pin) -> mã lệnh, xét theo ưu tiên."""
    return kiem_tra(
        "Dự án tuần 1 - Bộ ra quyết định lái xe",
        quyet_dinh_lai_xe,
        [
            Case(args=(1.5, 30, 5), expected="DUNG_KHAN_CAP",
                 mo_ta="vật cản 1.5 m, pin 5% - an toàn xét trước pin"),
            Case(args=(2.0, 30, 90), expected="DUNG_KHAN_CAP",
                 mo_ta="vật cản đúng 2.0 m - biên"),
            Case(args=(20.0, 40, 10), expected="VE_TRAM_SAC",
                 mo_ta="đường thoáng, pin 10%"),
            Case(args=(20.0, 40, 15), expected="BINH_THUONG",
                 mo_ta="pin đúng 15% - biên, chưa phải về sạc"),
            Case(args=(30.0, 75, 90), expected="GIAM_TOC",
                 mo_ta="tốc độ 75 km/h"),
            Case(args=(4.0, 50, 90), expected="GIAM_TOC",
                 mo_ta="vật cản 4.0 m"),
            Case(args=(30.0, 50, 90), expected="BINH_THUONG",
                 mo_ta="mọi thứ trong ngưỡng"),
        ],
    )


# ==========================================================================
# Phần dữ liệu cảm biến: bài mới của tuần 1
# ==========================================================================

def _nmea_tham_chieu(chuoi, huong):
    """Đáp án tham chiếu: ddmm.mmmmm -> độ thập phân, S và W là số âm."""
    if chuoi == "":
        return None
    x = float(chuoi)
    do = x // 100 + (x % 100) / 60
    return -do if huong in ("S", "W") else do


def kiem_tra_1_3(thoi_gian_mau, khoang_cach_m) -> bool:
    """thoi_gian_mau, khoang_cach_m -> hai cột của dòng "113.00,735.6"."""
    return kiem_tra_gia_tri(
        "Bài 1.3 - Một dòng LiDAR",
        [
            ('thoi_gian_mau ("113.00,735.6")', thoi_gian_mau, 113.0),
            ("khoang_cach_m (735.6 cm đổi ra mét)", khoang_cach_m, 7.356),
        ],
    )


def kiem_tra_2_4(vi_do) -> bool:
    """vi_do -> độ thập phân của vĩ độ NMEA "2100.27089"."""
    return kiem_tra_gia_tri(
        "Bài 2.4 - Đổi toạ độ NMEA ra độ",
        [
            ('vi_do ("2100.27089")', vi_do, _nmea_tham_chieu("2100.27089", "N")),
        ],
    )


def kiem_tra_2_5(gio_vn, phut_vn, giay_vn) -> bool:
    """gio_vn, phut_vn, giay_vn -> đổi "170030.00" UTC sang giờ Việt Nam."""
    return kiem_tra_gia_tri(
        "Bài 2.5 - Giờ UTC sang giờ Việt Nam",
        [
            ('gio_vn ("170030.00" UTC)', gio_vn, 0),
            ('phut_vn ("170030.00" UTC)', phut_vn, 0),
            ('giay_vn ("170030.00" UTC)', giay_vn, 30),
        ],
    )


def kiem_tra_3_3(trang_thai_fix_1, trang_thai_fix_2, trang_thai_fix_3) -> bool:
    """trang_thai_fix_* -> phân loại mã fix GPS 5, 0, 3 theo bảng."""
    return kiem_tra_gia_tri(
        "Bài 3.3 - Trạng thái fix GPS",
        [
            ("trang_thai_fix_1 (ma_fix_1 = 5)", trang_thai_fix_1, "RTK_FLOAT"),
            ("trang_thai_fix_2 (ma_fix_2 = 0)", trang_thai_fix_2, "KHONG_FIX"),
            ("trang_thai_fix_3 (ma_fix_3 = 3)", trang_thai_fix_3, "KHAC"),
        ],
    )


def kiem_tra_4_3(doc_khoang_cach) -> bool:
    """doc_khoang_cach(dong) -> khoảng cách mét, hoặc None khi dòng lỗi."""
    return kiem_tra(
        "Bài 4.3 - Hàm đọc một dòng LiDAR",
        doc_khoang_cach,
        [
            Case(args=("113.00,735.6\n",), expected=7.356,
                 mo_ta='doc_khoang_cach("113.00,735.6\n") - dòng bình thường'),
            Case(args=("20.00,1200.0\n",), expected=12.0,
                 mo_ta='doc_khoang_cach("20.00,1200.0\n") - tầm tối đa vẫn hợp lệ'),
            Case(args=("8.20,0.0\n",), expected=None,
                 mo_ta='doc_khoang_cach("8.20,0.0\n") - mất tín hiệu'),
            Case(args=("12.20,\n",), expected=None,
                 mo_ta='doc_khoang_cach("12.20,\n") - ô khoảng cách trống'),
            Case(args=("47.75,",), expected=None,
                 mo_ta='doc_khoang_cach("47.75,") - ô trống, không có \n'),
            Case(args=("113.10,653.5",), expected=6.535,
                 mo_ta='doc_khoang_cach("113.10,653.5") - không có \n'),
        ],
    )


def kiem_tra_4_4(nmea_sang_do) -> bool:
    """nmea_sang_do(chuoi, huong) -> độ thập phân, S/W âm, chuỗi rỗng là None."""
    return kiem_tra(
        "Bài 4.4 - Hàm đổi toạ độ",
        nmea_sang_do,
        [
            Case(args=("2100.27089", "N"), expected=_nmea_tham_chieu("2100.27089", "N"),
                 mo_ta='nmea_sang_do("2100.27089", "N") - vĩ độ Bắc'),
            Case(args=("10550.57792", "E"), expected=_nmea_tham_chieu("10550.57792", "E"),
                 mo_ta='nmea_sang_do("10550.57792", "E") - kinh độ Đông'),
            Case(args=("2100.27089", "S"), expected=_nmea_tham_chieu("2100.27089", "S"),
                 mo_ta='nmea_sang_do("2100.27089", "S") - hướng Nam là số âm'),
            Case(args=("10550.57792", "W"), expected=_nmea_tham_chieu("10550.57792", "W"),
                 mo_ta='nmea_sang_do("10550.57792", "W") - hướng Tây là số âm'),
            Case(args=("", "N"), expected=None,
                 mo_ta='nmea_sang_do("", "N") - chuỗi rỗng'),
            Case(args=("", "E"), expected=None,
                 mo_ta='nmea_sang_do("", "E") - chuỗi rỗng'),
        ],
    )


# ==========================================================================
# Bài 5: Vòng lặp và đọc file. Đáp án tính từ chính file trong data/.
# ==========================================================================

def _mo_data(ten_file):
    try:
        from .tien_ich_du_lieu import duong_dan_data
    except ImportError:  # khi chạy trực tiếp trong Colab, không qua package
        from tien_ich_du_lieu import duong_dan_data
    return open(duong_dan_data(ten_file), encoding="utf-8")


def _dap_an_5_1():
    hop_le = loi = 0
    with _mo_data("khoang_cach_truoc.csv") as f:
        next(f)
        for dong in f:
            o = dong.strip().split(",")[1]
            if o == "" or float(o) == 0.0:
                loi += 1
            else:
                hop_le += 1
    return hop_le, loi


def _dap_an_5_2():
    import csv
    with _mo_data("obd.csv") as f:
        toc_do = [int(hang["toc_do_kmh"]) for hang in csv.DictReader(f)]
    return max(toc_do), sum(toc_do) / len(toc_do)


def _dap_an_5_3():
    import csv
    with _mo_data("imu.csv") as f:
        for hang in csv.DictReader(f):
            if float(hang["ax"]) < -5.0:
                return float(hang["thoi_gian_s"])
    return None


def _dap_an_5_4():
    dem = 0
    with _mo_data("gps.nmea") as f:
        for dong in f:
            if dong.startswith("$GNGGA") and dong.split(",")[6] == "4":
                dem += 1
    return dem


def kiem_tra_5_1(so_mau_hop_le, so_mau_loi) -> bool:
    """so_mau_hop_le, so_mau_loi -> đếm dòng của khoang_cach_truoc.csv."""
    hop_le, loi = _dap_an_5_1()
    return kiem_tra_gia_tri(
        "Bài 5.1 - Đếm mẫu LiDAR hợp lệ",
        [
            ("so_mau_hop_le (khoang_cach_truoc.csv)", so_mau_hop_le, hop_le),
            ("so_mau_loi (khoang_cach_truoc.csv)", so_mau_loi, loi),
        ],
    )


def kiem_tra_5_2(toc_do_max, toc_do_tb) -> bool:
    """toc_do_max, toc_do_tb -> tốc độ lớn nhất và trung bình của obd.csv."""
    lon_nhat, trung_binh = _dap_an_5_2()
    return kiem_tra_gia_tri(
        "Bài 5.2 - Thống kê tốc độ OBD",
        [
            ("toc_do_max (obd.csv)", toc_do_max, lon_nhat),
            ("toc_do_tb (obd.csv, trung bình mọi mẫu)", toc_do_tb, trung_binh),
        ],
    )


def kiem_tra_5_3(t_phanh_gap) -> bool:
    """t_phanh_gap -> thời điểm đầu tiên ax < -5.0 trong imu.csv."""
    return kiem_tra_gia_tri(
        "Bài 5.3 - Tìm thời điểm phanh gấp",
        [
            ("t_phanh_gap (imu.csv, ax đầu tiên < -5.0)", t_phanh_gap, _dap_an_5_3()),
        ],
    )


def kiem_tra_5_4(so_giay_rtk_fixed) -> bool:
    """so_giay_rtk_fixed -> số câu $GNGGA có mã fix 4 trong gps.nmea."""
    return kiem_tra_gia_tri(
        "Bài 5.4 - Đếm số giây RTK fixed",
        [
            ("so_giay_rtk_fixed (gps.nmea, mã fix 4)", so_giay_rtk_fixed, _dap_an_5_4()),
        ],
    )


def kiem_tra_5_5(quang_duong_phanh) -> bool:
    """quang_duong_phanh(v0_kmh, gia_toc, dt) -> gần v0^2 / (2a), sai lệch tối đa v0 * dt."""

    def tham_chieu(v0_kmh, gia_toc):
        return (v0_kmh / 3.6) ** 2 / (2 * gia_toc)

    def trong_sai_so(ket_qua, v0_kmh, gia_toc, dt):
        return (isinstance(ket_qua, (int, float)) and not isinstance(ket_qua, bool)
                and abs(ket_qua - tham_chieu(v0_kmh, gia_toc)) <= (v0_kmh / 3.6) * dt + 1e-9)

    def ham_cham(v0_kmh, gia_toc, dt):
        ket_qua = quang_duong_phanh(v0_kmh, gia_toc, dt)
        # Trong sai số thì trả đúng đáp án tham chiếu, ngoài sai số thì giữ nguyên giá trị của học viên.
        return tham_chieu(v0_kmh, gia_toc) if trong_sai_so(ket_qua, v0_kmh, gia_toc, dt) else ket_qua

    cac_bo = [
        (72, 5.0, 0.01, "v0 = 72 km/h, a = 5.0, dt = 0.01"),
        (36, 4.0, 0.1, "v0 = 36 km/h, a = 4.0, dt = 0.1 - bước lớn"),
        (54, 7.0, 0.001, "v0 = 54 km/h, a = 7.0, dt = 0.001 - bước nhỏ"),
        (108, 6.0, 0.05, "v0 = 108 km/h, a = 6.0, dt = 0.05"),
        (0, 5.0, 0.01, "v0 = 0 km/h - xe đang đứng yên"),
    ]
    return kiem_tra(
        "Bài 5.5 - Quãng đường phanh",
        ham_cham if callable(quang_duong_phanh) else quang_duong_phanh,
        [Case(args=(v0, a, dt), expected=tham_chieu(v0, a),
              mo_ta=f"quang_duong_phanh({v0}, {a}, {dt}) - {mo_ta}")
         for v0, a, dt, mo_ta in cac_bo],
    )


# ==========================================================================
# Dự án: chạy quyet_dinh_lai_xe trên cả chuyến xe. Đáp án tính từ data/.
# ==========================================================================

def _quyet_dinh_tham_chieu(khoang_cach, toc_do, muc_pin):
    if khoang_cach <= 2.0:
        return "DUNG_KHAN_CAP"
    if muc_pin < 15:
        return "VE_TRAM_SAC"
    if khoang_cach <= 5.0 or toc_do > 60:
        return "GIAM_TOC"
    return "BINH_THUONG"


def _dap_an_lab():
    try:
        from .tien_ich_du_lieu import doc_chuyen_xe
    except ImportError:  # khi chạy trực tiếp trong Colab, không qua package
        from tien_ich_du_lieu import doc_chuyen_xe
    dem = {"DUNG_KHAN_CAP": 0, "VE_TRAM_SAC": 0, "GIAM_TOC": 0, "BINH_THUONG": 0}
    t_dung_dau_tien = None
    for t, khoang_cach, toc_do, pin in doc_chuyen_xe():
        if khoang_cach is None:
            continue
        lenh = _quyet_dinh_tham_chieu(khoang_cach, toc_do, pin)
        dem[lenh] += 1
        if lenh == "DUNG_KHAN_CAP" and t_dung_dau_tien is None:
            t_dung_dau_tien = t
    return dem, t_dung_dau_tien


def kiem_tra_lab(so_lan_dung, so_lan_ve_sac, so_lan_giam_toc, so_lan_binh_thuong,
                 t_dung_dau_tien) -> bool:
    """Đếm số giây của từng lệnh khi chạy quyet_dinh_lai_xe qua cả chuyến xe."""
    dem, t_dung = _dap_an_lab()
    return kiem_tra_gia_tri(
        "Dự án phần 2 - Chạy trên cả chuyến xe",
        [
            ("so_lan_dung (DUNG_KHAN_CAP)", so_lan_dung, dem["DUNG_KHAN_CAP"]),
            ("so_lan_ve_sac (VE_TRAM_SAC)", so_lan_ve_sac, dem["VE_TRAM_SAC"]),
            ("so_lan_giam_toc (GIAM_TOC)", so_lan_giam_toc, dem["GIAM_TOC"]),
            ("so_lan_binh_thuong (BINH_THUONG)", so_lan_binh_thuong, dem["BINH_THUONG"]),
            ("t_dung_dau_tien (giây DUNG_KHAN_CAP đầu tiên)", t_dung_dau_tien, t_dung),
        ],
    )
