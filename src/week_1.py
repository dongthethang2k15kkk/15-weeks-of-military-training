# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dongthethang2k15kkk/15-weeks-of-military-training/blob/main/week1/week_1.ipynb)
#
# # Tuần 1 — Nền tảng & Cú pháp cơ bản
#
# ![Kết quả cuối tuần 1](https://raw.githubusercontent.com/dongthethang2k15kkk/15-weeks-of-military-training/main/assets/ket_qua_tuan1.png)
#
# Cuối tuần bạn sẽ tự vẽ ra hình này từ dữ liệu của một chuyến xe.
#
# **Mục tiêu sau tuần này, bạn phải làm được:**
#
# 1. Khai báo biến đúng quy ước và phân biệt 4 kiểu dữ liệu cơ bản.
# 2. Dùng thành thạo toán tử số học và định dạng chuỗi bằng f-string.
# 3. Viết được logic ra quyết định bằng `if / elif / else`.
# 4. Gói một khối lệnh thành hàm bằng `def` và `return`, gọi lại với nhiều đầu vào.
# 5. Lặp lại một việc bằng `for` và `while`.
# 6. Đọc và xử lý file log cảm biến (CSV, NMEA) của một chuyến xe.
#
# **Quy tắc:** không sửa nội dung các ô kiểm tra. Chỉ viết code vào chỗ có `# TODO`
# hoặc chỗ được đánh dấu là chỗ viết của bạn.

# %%
# Ô thiết lập - chạy đầu tiên, mỗi lần mở notebook.
import os
import sys
import urllib.request

REPO_RAW = "https://raw.githubusercontent.com/dongthethang2k15kkk/15-weeks-of-military-training/main"

# File của tuần này. Chỉ tải file chưa có trên máy.
FILE_TESTS = ("runner.py", "test_week1.py", "tien_ich_du_lieu.py")
FILE_DATA = ("khoang_cach_truoc.csv", "gps.nmea", "obd.csv", "imu.csv")

# Mở notebook từ thư mục week1/ trên máy: lùi ra thư mục gốc, nơi có sẵn tests/.
if not os.path.isdir("tests") and os.path.isdir(os.path.join("..", "tests")):
    os.chdir("..")

for thu_muc, danh_sach in (("tests", FILE_TESTS), ("data", FILE_DATA)):
    os.makedirs(thu_muc, exist_ok=True)
    for ten_file in danh_sach:
        duong_dan = os.path.join(thu_muc, ten_file)
        if not os.path.isfile(duong_dan):
            urllib.request.urlretrieve(f"{REPO_RAW}/{thu_muc}/{ten_file}", duong_dan)
open(os.path.join("tests", "__init__.py"), "a").close()

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

from tests.test_week1 import (
    kiem_tra_1_1,
    kiem_tra_1_2,
    kiem_tra_1_3,
    kiem_tra_2_1,
    kiem_tra_2_2,
    kiem_tra_2_3,
    kiem_tra_2_4,
    kiem_tra_2_5,
    kiem_tra_3_1,
    kiem_tra_3_2,
    kiem_tra_3_3,
    kiem_tra_4_1,
    kiem_tra_4_2,
    kiem_tra_4_3,
    kiem_tra_4_4,
    kiem_tra_5_1,
    kiem_tra_5_2,
    kiem_tra_5_3,
    kiem_tra_5_4,
    kiem_tra_5_5,
    kiem_tra_du_an,
    kiem_tra_lab,
)

print("Moi truong san sang. Phien ban Python:", sys.version.split()[0])

# %% [markdown]
# ---
# ## Cách làm bài và chấm bài
#
# Mỗi bài tập gồm hai ô đi liền nhau: ô bạn viết code, và ô kiểm tra ngay dưới nó.
# Ô kiểm tra đọc các biến hoặc hàm mà ô trên tạo ra, nên **tên phải khớp từng chữ**.
#
# Chạy thử một lượt với bài mẫu dưới đây trước khi vào bài thật.
#
# Đề: gán biến `vi_du_tong` bằng tổng của `3` và `4`.

# %%
vi_du_tong = None  # sửa dòng này: thay None bằng 3 + 4

# %% [markdown]
# Ô ngay trên là chỗ bạn viết. Sửa `None` thành `3 + 4`, rồi bấm Shift+Enter để chạy
# ô đó. Sau đó bấm Shift+Enter tiếp ở ô dưới đây để chấm.

# %%
if vi_du_tong == 7:
    print("PASS - ban da lam dung, sang Bai 1 duoc roi")
else:
    print(f"FAIL - mong doi 7, thuc te {vi_du_tong}")

# %% [markdown]
# Ba điều rút ra, áp dụng cho mọi bài trong khoá:
#
# 1. Sửa xong ô code phải **chạy lại chính ô đó** rồi mới chạy ô kiểm tra. Bỏ qua
#    bước này thì ô kiểm tra vẫn đọc giá trị cũ, và bạn sẽ thấy FAIL dù đã sửa đúng.
# 2. Chưa làm gì mà chạy ô kiểm tra thì nó báo FAIL kèm dòng "thực tế: None". Đó là
#    trạng thái bình thường lúc mới mở notebook.
# 3. Dòng "mong đợi" trong báo lỗi cho biết đáp án đúng phải trông ra sao. So nó với
#    dòng "thực tế" để biết lệch ở đâu.
#
# Chạy lại cả notebook từ đầu bằng `Runtime > Restart and run all` nếu thấy kết quả
# lộn xộn không giải thích được.

# %% [markdown]
# ---
# ## Bài 1 — Biến và kiểu dữ liệu
#
# #### 📖 Cú pháp
#
# | Cú pháp | Nghĩa | Ví dụ |
# |---|---|---|
# | `ten_bien = gia_tri` | gán giá trị cho biến (biến là một cái tên gắn với một giá trị trong bộ nhớ, kiểu được suy ra từ giá trị, không cần khai báo trước) | `toc_do_dong_co = 120` |
# | `int` | kiểu số nguyên | `toc_do_dong_co = 120` (vòng/phút) |
# | `float` | kiểu số thực | `dien_ap_pin = 11.5` (V) |
# | `str` | kiểu chuỗi ký tự, đặt trong dấu nháy | `trang_thai_he_thong = "Dang chay"` |
# | `bool` | kiểu đúng/sai, chỉ có `True` và `False` | `cam_bien_hoat_dong = True` |
# | `snake_case` | quy ước đặt tên biến (PEP 8): viết thường, các từ nối bằng dấu gạch dưới | `so_lan_doc_cam_bien` |
# | `VIET_HOA` | quy ước đặt tên hằng số: viết hoa toàn bộ | `TOC_DO_TOI_DA = 150` |
# | `print(x)` | in giá trị `x` ra màn hình | `print(11.5)` → `11.5` |
# | `type(x)` | cho biết kiểu dữ liệu của `x` | `type(11.5)` → `<class 'float'>` |
# | `int(x)` | ép `x` sang số nguyên | `int("10")` → `10`, `int(10.9)` → `10` |
# | `float(x)` | ép `x` sang số thực | `float("10.5")` → `10.5` |
# | `round(x)` HOẶC `round(x, n)` | làm tròn `x` đến `n` chữ số sau dấu phẩy | `round(10.9)` → `11`, `round(10.9, 0)` → `11.0` |
# | `a + b` | cộng hai số, hoặc nối hai chuỗi | `10 + 5` → `15`, `"10" + "5"` → `"105"` |
# | `dong.split(",")[i]` | cắt dòng chữ theo dấu phẩy, lấy cột thứ `i` (đếm từ 0) | `"1.5,302.0".split(",")[1]` → `"302.0"` |
# | `dong.strip()` | bỏ khoảng trắng và ký tự xuống dòng ở hai đầu chuỗi | `"5\n".strip()` → `"5"` |
#
# #### ⚠️ Lỗi hay gặp
#
# - `int("10.5")` báo `ValueError` vì `int()` không đọc được dấu chấm. Ép qua `float()`
#   trước: `int(float("10.5"))`.
# - Chuỗi gõ từ bàn phím hoặc cắt từ một dòng chữ luôn có kiểu `str`, phải ép kiểu
#   trước khi tính: `float("302.0")`, `int(input("So xe: "))`.
# - `int(10.9)` cho `10` vì **cắt bỏ phần thập phân** (truncation), còn `round(10.9)`
#   cho `11`.
# - `int("10") + int("5")` là **phép cộng đại số**, cho `15`. `int("10" + "5")` là
#   **nối chuỗi** `"10"` với `"5"` thành `"105"` rồi mới ép kiểu, cho `105`.
# - Dùng biến chưa gán thì Python báo `NameError`.
# - Nên đặt tên theo nội dung: `toc_do_xe`, `so_lan_doc_cam_bien`, không đặt kiểu `x`,
#   `a1`.

# %%
# 💻 Ví dụ: bốn kiểu dữ liệu và hằng số
toc_do_dong_co = 120               # int
dien_ap_pin = 11.5                 # float
trang_thai_he_thong = "Dang chay"  # str
cam_bien_hoat_dong = True          # bool

TOC_DO_TOI_DA = 150                # hằng số: viết HOA

print(toc_do_dong_co, type(toc_do_dong_co))     # lệnh type() để check kiểu dữ liệu
print(dien_ap_pin, type(dien_ap_pin))
print(trang_thai_he_thong, type(trang_thai_he_thong))
print(cam_bien_hoat_dong, type(cam_bien_hoat_dong))

# %% [markdown]
# `"10"` và `10` là hai thứ khác nhau, `int()` và `float()` chỉ ép được chuỗi đúng
# định dạng số.

# %%
# 💻 Ví dụ: ép kiểu chuỗi sang số
print(int("10"))               # 10 - toàn chữ số, ép được
# print(int("10.5"))           # Bỏ dấu # để thấy lỗi ValueError
print(int(float("10.5")))      # 10 - ép qua float() trước rồi mới int() sau

# %% [markdown]
# Muốn ra số nguyên từ chuỗi có dấu chấm thì ép qua `float()` trước rồi mới `int()`.

# %%
# 💻 Ví dụ: int() và round()
print(int(10.9))     # 10 - cắt bỏ phần thập phân
print(round(10.9))   # 11 - làm tròn theo quy tắc toán học

# %% [markdown]
# Hai hàm cho hai kết quả khác nhau.

# %%
# 💻 Ví dụ: dùng biến chưa gán
# print(bien_chua_gan)   # Bỏ dấu # để thấy lỗi NameError

# %% [markdown]
# Biến phải được gán trước khi dùng.

# %%
# 💻 Ví dụ: dấu + với số và với chuỗi
print(int("10") + int("5"))   # 15 - ép hai chuỗi thành số rồi mới cộng
print(int("10" + "5"))        # 105 - nối chuỗi "10" với "5" trước rồi mới ép

# %% [markdown]
# Cùng các ký tự `1`, `0`, `5` nhưng thứ tự thao tác khác nhau cho hai kết quả khác
# nhau.

# %%
# 💻 Ví dụ: bool và số nguyên
print(type(True), True == 1)   # <class 'bool'> True

# %% [markdown]
# `type(True)` trả về `bool`, không phải `int`, dù `True == 1` vẫn đúng.

# %% [markdown]
# ### 🎯 Bài tập 1.1 — Trung bình lần đọc cảm biến
#
# Cảm biến khoảng cách bị nhiễu nên đọc 3 lần liên tiếp cho một cảm biến. Có hai
# cảm biến. Với mỗi cảm biến, gán biến `tb_doc_*` bằng trung bình cộng ba lần đọc.

# %%
doc_1_1, doc_1_2, doc_1_3 = 8, 9, 10
doc_2_1, doc_2_2, doc_2_3 = 7.5, 6, 8

tb_doc_1 = None  # TODO: trung bình cộng của doc_1_1, doc_1_2, doc_1_3
tb_doc_2 = None  # TODO: trung bình cộng của doc_2_1, doc_2_2, doc_2_3

# %%
kiem_tra_1_1(tb_doc_1, tb_doc_2)

# %% [markdown]
# ### 🎯 Bài tập 1.2 — Ép kiểu dữ liệu
#
# Cho chuỗi `gia_tri_tho_2`. Gán `noi_chuoi` bằng cách nối nó với chuỗi `"5"`, và
# gán `tong_so` bằng cách ép nó sang số nguyên rồi cộng thêm `5`. Xem lại ô ví dụ
# ngay phía trên nếu chưa rõ khác nhau ở đâu.

# %%
gia_tri_tho_2 = "20"

noi_chuoi = None  # TODO: gia_tri_tho_2 nối với "5"
tong_so = None    # TODO: ép gia_tri_tho_2 sang int rồi cộng 5

# %%
kiem_tra_1_2(noi_chuoi, tong_so)

# %% [markdown]
# ### 📡 Bài tập 1.3 — Một dòng LiDAR
#
# Dòng `dong_kc` lấy từ `data/khoang_cach_truoc.csv`, ghi của cảm biến LiDAR 1D gắn
# phía trước xe, tại giây 113.00 của chuyến. Hai cột là thời gian (giây) và khoảng
# cách tới vật phía trước (cm).
#
# Gán `thoi_gian_mau` (float, giây) và `khoang_cach_m` (float, mét).
#
# Ví dụ: dòng `"113.05,694.5\n"` cho `thoi_gian_mau = 113.05`, `khoang_cach_m = 6.945`.

# %%
# 💻 Ví dụ: lấy một cột từ dòng log
dong_1, dong_2 = "5.00,1200.0\n", "113.05,694.5\n"
print(float(dong_1.strip().split(",")[1]) / 100)   # strip() bỏ "\n", split(",") cắt theo dấu phẩy, [1] lấy cột 1
print(float(dong_2.strip().split(",")[1]) / 100)

# %%
dong_kc = "113.00,735.6\n"

thoi_gian_mau = None  # TODO: float, giây
khoang_cach_m = None  # TODO: float, mét

# %%
kiem_tra_1_3(thoi_gian_mau, khoang_cach_m)

# %% [markdown]
# ---
# ## Bài 2 — Toán tử, chuỗi và ép kiểu
#
# #### 📖 Cú pháp
#
# | Cú pháp | Nghĩa | Ví dụ |
# |---|---|---|
# | `+`, `-`, `*` | cộng, trừ, nhân | `7 * 3` → `21` |
# | `/` | chia, luôn trả về `float` | `10 / 2` → `5.0` |
# | `//` | chia lấy phần nguyên | `17 // 5` → `3` |
# | `%` | chia lấy phần dư, kết quả luôn từ `0` đến `b - 1`, hay dùng để chia chu kỳ, đổi đơn vị | `17 % 5` → `2`, `gio % 24` luôn ra giờ từ 0 đến 23 |
# | `**` | lũy thừa (mũ) | `2 ** 3` → `8` |
# | `a == (a // b) * b + a % b` | quan hệ luôn đúng giữa `//` và `%` khi `a`, `b` là số nguyên dương: `//` cho thương, `%` cho số dư | `17 == 3 * 5 + 2` |
# | `f"...{x}..."` | f-string: đặt `f` trước dấu nháy, nhúng biểu thức vào giữa cặp ngoặc nhọn `{}` | `f"{3 * 4} km"` → `"12 km"` |
# | `{x:.2f}` | trong f-string, hiển thị `x` với 2 chữ số sau dấu phẩy, giá trị của `x` giữ nguyên | `f"{7.1666:.2f}"` → `"7.17"` |
# | `round(x, n)` | làm tròn giá trị `x` đến `n` chữ số sau dấu phẩy, giá trị đổi thật | `round(7.1666, 2)` → `7.17` |
# | `str(x)` | ép `x` sang chuỗi | `str(50)` → `"50"` |
# | `input("lời nhắc")` | đọc chữ gõ từ bàn phím, luôn trả về `str` | `int(input("So xe: "))` |
#
# #### ⚠️ Lỗi hay gặp
#
# - Ghép chuỗi với số bằng `+` báo `TypeError`, phải gọi `str()` cho từng số:
#   `"Toc do: " + str(50)`. f-string tự làm việc đó nên ngắn hơn và ít lỗi hơn.
# - `//` giữa hai `int` cho `int`. Có một vế là `float` thì kết quả cũng là `float`:
#   `7.0 // 2` ra `3.0`.
# - Với số âm, `//` làm tròn về phía âm vô cực: `-7 // 2` ra `-4`.
# - `{x:.2f}` chỉ đổi cách hiển thị. Khi đề bài yêu cầu trả về một số đã làm tròn
#   (không chỉ in ra), phải dùng `round()`.

# %%
# 💻 Ví dụ: đổi giây sang giờ, phút, giây
tong_giay = 3725

gio_vd = tong_giay // 3600
phut_vd = (tong_giay % 3600) // 60
giay_vd = tong_giay % 60

print(f"Thoi gian chay: {gio_vd} gio {phut_vd} phut {giay_vd} giay")

# %% [markdown]
# Cùng công thức áp dụng được cho nhiều xe cùng lúc, không chỉ một giá trị lẻ.

# %%
# 💻 Ví dụ: cùng công thức cho hai xe
tong_giay_a, tong_giay_b = 3725, 7260

print(f"Xe A: {tong_giay_a // 3600} gio {(tong_giay_a % 3600) // 60} phut {tong_giay_a % 60} giay")
print(f"Xe B: {tong_giay_b // 3600} gio {(tong_giay_b % 3600) // 60} phut {tong_giay_b % 60} giay")

# %% [markdown]
# Hai dòng, hai xe, cùng một công thức `// 3600`, `% 3600 // 60`, `% 60`.

# %%
# 💻 Ví dụ: ghép chuỗi bằng + và bằng f-string
toc_do = 50

# print("Toc do: " + toc_do)               # Bỏ dấu # để thấy lỗi TypeError
print("Toc do: " + str(toc_do) + " km/h")  # ghép bằng +, phải ép str() cho số
print(f"Toc do: {toc_do} km/h")            # f-string tự ép

# %%
# 💻 Ví dụ: tính chất của // và %
a, b = 17, 5
print(a // b, a % b, (a // b) * b + a % b)   # 3 2 17 -> cong thuc dung
print(7.0 // 2)                               # 3.0 - float vi co toan hang float
print(-7 // 2)                                # -4 - lam tron ve am vo cuc

# %%
# 💻 Ví dụ: round() và {:.2f}
gia_goc = 21.5 / 3

gia_lam_tron = round(gia_goc, 2)         # giá trị thật sự đổi thành 7.17
print(gia_lam_tron, type(gia_lam_tron))

print(f"{gia_goc:.2f}")                  # chỉ đổi cách hiển thị, gia_goc vẫn là 7.1666...
print(gia_goc)

# %% [markdown]
# ### 🎯 Bài tập 2.1 — Chia tiền sạc
#
# Một nhóm xe sạc chung một trụ. Trạm tính thêm phí dịch vụ bằng phần trăm trên tiền
# điện. Có hai lượt sạc, mỗi lượt cho sẵn `tong_tien_sac`, `phan_tram_phi_dv`, `so_xe`.
#
# Công thức, trong đó $m$ là `moi_xe_tra`, $T$ là `tong_tien_sac`, $p$ là
# `phan_tram_phi_dv` và $n$ là `so_xe`:
#
# $$m = \frac{T \times \left(1 + \dfrac{p}{100}\right)}{n}$$
#
# Làm tròn 2 chữ số bằng `round()`. Với mỗi lượt, gán `moi_xe_tra_*` theo công thức
# này.
#
# Ví dụ: `tong_tien_sac = 200000`, `phan_tram_phi_dv = 20`, `so_xe = 4` cho
# `moi_xe_tra = 60000.0`.

# %%
tong_tien_sac_1, phan_tram_phi_dv_1, so_xe_1 = 300000, 10, 3
tong_tien_sac_2, phan_tram_phi_dv_2, so_xe_2 = 100000, 15, 3

moi_xe_tra_1 = None  # TODO: lượt sạc 1
moi_xe_tra_2 = None  # TODO: lượt sạc 2

# %%
kiem_tra_2_1(moi_xe_tra_1, moi_xe_tra_2)

# %% [markdown]
# ### 🎯 Bài tập 2.2 — Báo cáo quãng đường
#
# Gán `bao_cao` bằng một chuỗi(f-string) đúng theo mẫu:
#
# ```
# Xe đã đi được {quang_duong} mét trong {thoi_gian} giây.
# ```
#
# Trong đó quãng đường $s = v \times t$, với $v$ là `van_toc_bc` và $t$ là
# `thoi_gian_bc`, không làm tròn. Dấu chấm cuối câu và dấu tiếng Việt phải khớp chính
# xác.
#
# Ví dụ: `van_toc_bc = 10.0`, `thoi_gian_bc = 5` cho chuỗi
# `"Xe đã đi được 50.0 mét trong 5 giây."`.

# %%
van_toc_bc, thoi_gian_bc = 20.0, 3

bao_cao = None  # TODO: tính quãng đường rồi gán chuỗi đúng mẫu bằng f-string

# %%
kiem_tra_2_2(bao_cao)

# %% [markdown]
# ### 💻 Ô tự do — thử `input()`
#
# Bỏ dấu `#` để chạy thử.

# %%
# tong = float(input("Tong tien sac: "))
# xe = int(input("So xe: "))
# print(f"Moi xe tra {tong / xe:.2f}")

# %% [markdown]
# ### 🎯 Bài tập 2.3 — Đổi giây sang giờ phút giây
#
# Ô ví dụ ở đầu Bài 2 đổi `tong_giay = 3725` sang giờ/phút/giây.
# Làm lại đúng phép tính đó cho `tong_giay_bt = 5000`, gán vào `gio`, `phut`, `giay`.

# %%
tong_giay_bt = 5000

gio = None   # TODO
phut = None  # TODO
giay = None  # TODO

# %%
kiem_tra_2_3(gio, phut, giay)

# %% [markdown]
# ### 📡 Bài tập 2.4 — Đổi toạ độ NMEA ra độ
#
# Module GNSS ghi toạ độ vào `data/gps.nmea` dạng `ddmm.mmmmm`: hai chữ số đầu là
# độ, phần còn lại là phút. Dòng `$GNGGA` đầu tiên của file (giây 0 của chuyến) có vĩ
# độ `2100.27089`.
#
# Gọi $x$ là chuỗi đó đã ép sang số. Công thức đổi sang độ thập phân:
#
# $$\text{do} = \left\lfloor \frac{x}{100} \right\rfloor, \qquad \text{phut} = x \bmod 100, \qquad \varphi = \text{do} + \frac{\text{phut}}{60}$$
#
# Trong đó $\lfloor \cdot \rfloor$ là làm tròn xuống, $\bmod$ là phần dư của phép chia,
# $\varphi$ là vĩ độ thập phân. Gán `vi_do` (float) bằng $\varphi$, tính từ
# `chuoi_vi_do`.
#
# Ví dụ: `"2103.00000"` cho độ 21, phút 3, `vi_do = 21.05`.

# %%
chuoi_vi_do = "2100.27089"

vi_do = None  # TODO

# %%
kiem_tra_2_4(vi_do)

# %% [markdown]
# ### 📡 Bài tập 2.5 — Giờ UTC sang giờ Việt Nam
#
# Câu `$GNGGA` ghi giờ UTC dạng `hhmmss.ss`. Chuỗi `chuoi_gio_utc` lấy từ dòng
# `$GNGGA,170030.00,...` của `data/gps.nmea`, tức giây 90 của chuyến: 17 giờ 00 phút
# 30 giây UTC.
#
# Gọi $x$ là phần nguyên của chuỗi đã ép sang số (ở đây là `170030`). Tách giờ, phút,
# giây UTC:
#
# $$h = \left\lfloor \frac{x}{10000} \right\rfloor, \qquad \text{phut} = \left\lfloor \frac{x}{100} \right\rfloor \bmod 100, \qquad \text{giay} = x \bmod 100$$
#
# Giờ Việt Nam chênh UTC 7 tiếng, phút và giây giữ nguyên:
#
# $$h_{\text{VN}} = (h + 7) \bmod 24$$
#
# Gán `gio_vn` bằng $h_{\text{VN}}$, `phut_vn` bằng phút, `giay_vn` bằng giây (cả ba là
# `int`).
#
# Ví dụ: `"084512.00"` cho 15 giờ 45 phút 12 giây. `"182000.00"` cho 1 giờ 20 phút
# 0 giây.

# %%
chuoi_gio_utc = "170030.00"

gio_vn = None   # TODO
phut_vn = None  # TODO
giay_vn = None  # TODO

# %%
kiem_tra_2_5(gio_vn, phut_vn, giay_vn)

# %% [markdown]
# ---
# ## Bài 3 — Boolean và câu lệnh điều kiện
#
# #### 📖 Cú pháp
#
# | Cú pháp | Nghĩa | Ví dụ |
# |---|---|---|
# | `==` | bằng | `3 == 3` → `True` |
# | `!=` | khác (không bằng) | `3 != 4` → `True` |
# | `>`, `<` | lớn hơn, bé hơn | `5 > 3` → `True` |
# | `>=`, `<=` | lớn hơn hoặc bằng, bé hơn hoặc bằng | `2.0 <= 2.0` → `True` |
# | `and` | cả hai vế cùng đúng | `True and False` → `False` |
# | `or` | một trong hai vế đúng | `True or False` → `True` |
# | `not` | đảo ngược từ đúng thành sai và ngược lại | `not True` → `False` |
# | `if dieu_kien:` | chạy khối lệnh thụt lề bên dưới khi điều kiện đúng | `if khoang_cach <= 2.0:` |
# | `elif dieu_kien:` | xét điều kiện tiếp theo khi các nhánh trên đều sai | `elif khoang_cach <= 5.0:` |
# | `else:` | chạy khi mọi nhánh trên đều sai | `else:` |
# | thụt lề | khối lệnh được xác định bằng thụt lề, không dùng ngoặc nhọn. PEP 8 quy định 4 dấu cách cho mỗi cấp, ấn TAB để thụt lề đúng | dòng `if a > b:` rồi dòng sau thụt vào 4 dấu cách |
#
# Cấu trúc rẽ nhánh. Các nhánh được xét lần lượt từ trên xuống, gặp nhánh đúng đầu
# tiên là dừng, nên thứ tự các nhánh quyết định kết quả:
#
# ```python
# if dieu_kien_1:
#     ...
# elif dieu_kien_2:
#     ...
# else:
#     ...
# ```
#
# #### ⚠️ Lỗi hay gặp
#
# - Dùng `=` thay cho `==`. `=` là gán, `==` là so sánh, trong `if` phải dùng `==`.
# - Viết nhiều `if` liên tiếp thay vì `elif`. Nhiều `if` đứng riêng đều được xét *tất
#   cả*, nên biến kết quả có thể bị nhánh sau ghi đè lên nhánh trước.
# - Sai thứ tự nhánh. Đặt `if khoang_cach <= 5.0` lên trước thì khoảng cách 1.5 m
#   cũng rơi vào nhánh đó và không bao giờ chạm tới nhánh khẩn cấp.
# - Quên giá trị biên. Đề nói "nhỏ hơn hoặc bằng 2.0" thì phải là `<= 2.0`, không phải
#   `< 2.0`. Test luôn kiểm tra đúng chỗ này.
# - Thụt lề sai thì Python báo `IndentationError` và dừng chạy.

# %%
# 💻 Ví dụ: phân loại khoảng cách bằng if/elif/else
khoang_cach = 3.7

if khoang_cach <= 2.0:
    trang_thai_vi_du = "PHANH_KHAN_CAP"
elif khoang_cach <= 5.0:
    trang_thai_vi_du = "GIAM_TOC"
else:
    trang_thai_vi_du = "AN_TOAN"

print(f"Khoang cach {khoang_cach} m -> {trang_thai_vi_du}")

# %%
# 💻 Ví dụ: lỗi dùng = thay cho ==
# if khoang_cach = 3.7:   # Bỏ dấu # để thấy lỗi SyntaxError

# %% [markdown]
# ### 🎯 Bài tập 3.1 — Cảnh báo vật cản
#
# Cho `khoang_cach = 3.7`. Viết một khối `if/elif/else` gán kết quả vào biến
# `trang_thai` theo bảng:
#
# | Điều kiện | Kết quả |
# |---|---|
# | `khoang_cach <= 2.0` | `"PHANH_KHAN_CAP"` |
# | `khoang_cach <= 5.0` | `"GIAM_TOC"` |
# | còn lại | `"AN_TOAN"` |
#
# Ô kiểm tra đọc biến `trang_thai`, nên tên biến phải đúng từng chữ.

# %%
khoang_cach = 3.7

trang_thai = None  # khởi tạo sẵn, để ô kiểm tra chạy được khi bạn chưa làm gì

# Viết khối if/elif/else của bạn vào ngay dưới dòng này:


# %%
kiem_tra_3_1(trang_thai)

# %% [markdown]
# ### 🎯 Bài tập 3.2 — Giới hạn tốc độ
#
# Giới hạn phụ thuộc hai thứ: loại đường và trời có mưa hay không.
#
# | `loai_duong` | Khô ráo | Trời mưa |
# |---|---|---|
# | `"khu_truong_hoc"` | 30 | 30 |
# | `"khu_dan_cu"` | 50 | 40 |
# | `"duong_tinh"` | 80 | 60 |
# | `"cao_toc"` | 120 | 90 |
#
# Cho `loai_duong = "duong_tinh"` và `troi_mua = True`. Gán `gioi_han` bằng số
# km/h tương ứng (số nguyên).
#
# Bảng có hai chiều nên khối của bạn cũng có hai tầng: tầng ngoài xét `loai_duong`,
# bên trong mỗi nhánh mới xét `troi_mua`. Riêng `"khu_truong_hoc"` cho cùng một số
# ở cả hai cột nên nhánh đó không cần tầng trong.
#
# Khung chung của khối hai tầng, tầng trong thụt thêm 4 dấu cách so với tầng ngoài:
#
# ```python
# if dieu_kien_ngoai_1:
#     ket_qua = ...              # không cần tầng trong nếu chỉ có một giá trị
# elif dieu_kien_ngoai_2:
#     if dieu_kien_trong:
#         ket_qua = ...
#     else:
#         ket_qua = ...
# ```

# %%
loai_duong = "duong_tinh"
troi_mua = True

gioi_han = None  # khởi tạo sẵn, để ô kiểm tra chạy được khi bạn chưa làm gì

# Viết khối if/elif/else của bạn vào ngay dưới dòng này:


# %%
kiem_tra_3_2(gioi_han)

# %% [markdown]
# ### 📡 Bài tập 3.3 — Trạng thái fix GPS
#
# Cột 6 của câu `$GNGGA` (đếm từ 0, sau khi cắt theo dấu phẩy) là mã fix, cho biết
# module GPS định vị được bằng cách nào. Dòng giây 40 của `data/gps.nmea`:
#
# ```
# $GNGGA,165940.00,2100.35986,N,10550.57994,E,5,16,0.8,12.6,M,-22.1,M,1.0,0000*45
# ```
#
# có mã fix `5`. Gán `trang_thai_fix_*` theo bảng:
#
# | `ma_fix` | Kết quả |
# |---|---|
# | 0 | `"KHONG_FIX"` |
# | 1 | `"GPS"` |
# | 2 | `"DGPS"` |
# | 4 | `"RTK_FIXED"` |
# | 5 | `"RTK_FLOAT"` |
# | còn lại | `"KHAC"` |
#
# Ba mã cần phân loại: `ma_fix_1 = 5` (giây 40), `ma_fix_2 = 0` (giây 95, lúc xe
# chạy dưới tán cây, ô vĩ độ và kinh độ để trống) và `ma_fix_3 = 3` (mã không có
# trong bảng).
#
# Ví dụ: `ma_fix = 4` cho `"RTK_FIXED"`, `ma_fix = 1` cho `"GPS"`.

# %%
ma_fix_1, ma_fix_2, ma_fix_3 = 5, 0, 3

trang_thai_fix_1 = None  # khởi tạo sẵn, để ô kiểm tra chạy được khi bạn chưa làm gì
trang_thai_fix_2 = None
trang_thai_fix_3 = None

# Viết khối if/elif/else cho ma_fix_1 vào ngay dưới dòng này:


# Viết khối if/elif/else cho ma_fix_2 vào ngay dưới dòng này:


# Viết khối if/elif/else cho ma_fix_3 vào ngay dưới dòng này:


# %%
kiem_tra_3_3(trang_thai_fix_1, trang_thai_fix_2, trang_thai_fix_3)

# %% [markdown]
# ---
# ## Bài 4 — Hàm
#
# #### 📖 Cú pháp
#
# | Cú pháp | Nghĩa | Ví dụ |
# |---|---|---|
# | `def ten_ham(tham_so):` | định nghĩa hàm, tức đặt tên cho một khối code để gọi lại nhiều lần với đầu vào khác nhau. Dòng `def` kết thúc bằng dấu hai chấm `:`, thân hàm thụt vào 4 dấu cách. Tham số là tên nhận giá trị lúc gọi | `def gap_doi(x):` |
# | `ten_ham(gia_tri)` | gọi hàm: thân hàm chạy lại từ đầu, `gia_tri` trong ngoặc được gán vào tham số | `gap_doi(5)` |
# | `def ten_ham(a, b):` | hàm nhiều tham số, ngăn cách bằng dấu phẩy | `gap_doi_tong(3, 4)` |
# | `return gia_tri` | kết thúc hàm ngay tại đó và gửi `gia_tri` ra nơi gọi, các dòng sau `return` trong cùng nhánh không bao giờ chạy | `return x * 2` |
# | `None` | giá trị "không có gì", là kết quả của hàm không có `return` | `print(khong_co_return(5))` → `None` |
# | `pass` | lệnh rỗng, giữ chỗ cho khối lệnh chưa viết | `pass` |
#
# #### ⚠️ Lỗi hay gặp
#
# - Định nghĩa hàm không chạy thân hàm. Thân hàm chỉ chạy khi có lời gọi
#   `ten_ham(...)`.
# - Quên `return`: tính đúng hết rồi mà hàm vẫn trả về `None`.
# - Tham số chỉ tồn tại bên trong hàm. Gọi tên tham số ở bên ngoài thì Python báo
#   `NameError`.

# %%
# 💻 Ví dụ: một hàm, nhiều lần gọi
def phan_loai_vi_du(khoang_cach):     # def: bắt đầu định nghĩa. Trong ngoặc là tham số
    if khoang_cach <= 2.0:
        ket_qua = "PHANH_KHAN_CAP"
    elif khoang_cach <= 5.0:
        ket_qua = "GIAM_TOC"
    else:
        ket_qua = "AN_TOAN"
    return ket_qua                    # return: gửi giá trị ra ngoài cho nơi gọi


print(phan_loai_vi_du(0.5))
print(phan_loai_vi_du(3.7))
print(phan_loai_vi_du(12.0))

# %% [markdown]
# Một khối code, ba lần gọi, ba kết quả. Không chép dòng nào.

# %%
# 💻 Ví dụ: hàm có return và hàm quên return
def khong_co_return(x):
    ket_qua = x * 2       # tính đúng nhưng không gửi ra ngoài


def co_return(x):
    return x * 2


print(khong_co_return(5))   # None - quên return
print(co_return(5))         # 10

# %%
# 💻 Ví dụ: gọi tham số ngoài hàm
# print(x)   # Bỏ dấu # để thấy lỗi NameError

# %% [markdown]
# ### 🎯 Bài tập 4.1 — Hàm cảnh báo vật cản
#
# Viết hàm `canh_bao_vat_can(khoang_cach)` trả về đúng chuỗi theo bảng ngưỡng của
# bài 3.1:
#
# | Điều kiện | Kết quả |
# |---|---|
# | `khoang_cach <= 2.0` | `"PHANH_KHAN_CAP"` |
# | `khoang_cach <= 5.0` | `"GIAM_TOC"` |
# | còn lại | `"AN_TOAN"` |
#
# Đây là bài 3.1 viết lại thành hàm. Logic giữ nguyên, việc của bạn là bọc nó trong
# `def` và đổi dòng gán cuối thành `return`. Bộ chấm sẽ tự gọi hàm với năm khoảng
# cách khác nhau, gồm cả hai giá trị biên `2.0` và `5.0`.

# %%
def canh_bao_vat_can(khoang_cach):
    # TODO: khối if/elif/else như bài 3.1, kết thúc bằng return
    pass #Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_4_1(canh_bao_vat_can)

# %% [markdown]
# ### 🎯 Bài tập 4.2 — Hàm giới hạn tốc độ
#
# Viết hàm `gioi_han_toc_do(loai_duong, troi_mua)` trả về số km/h theo đúng bảng ở
# bài 3.2. Hàm này nhận hai tham số, ngăn cách bằng dấu phẩy.
#
# | `loai_duong` | Khô ráo | Trời mưa |
# |---|---|---|
# | `"khu_truong_hoc"` | 30 | 30 |
# | `"khu_dan_cu"` | 50 | 40 |
# | `"duong_tinh"` | 80 | 60 |
# | `"cao_toc"` | 120 | 90 |
#
# Bộ chấm gọi hàm bảy lần, phủ cả bốn loại đường và cả hai điều kiện thời tiết.

# %%
def gioi_han_toc_do(loai_duong, troi_mua):
    # TODO: khối if/elif/else hai tầng như bài 3.2, kết thúc bằng return
    pass  #Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_4_2(gioi_han_toc_do)

# %% [markdown]
# ### 📡 Bài tập 4.3 — Hàm đọc một dòng LiDAR
#
# `data/khoang_cach_truoc.csv` có hai loại dòng lỗi cần bỏ qua: ô khoảng cách để trống
# (ví dụ `9.75,`) và khoảng cách `0.0`, tức cảm biến mất tín hiệu (ví dụ `6.70,0.0`).
# Tầm đo tối đa `1200.0` là giá trị hợp lệ.
#
# Viết hàm `doc_khoang_cach(dong)` nhận một dòng chữ của file, trả về khoảng cách theo
# mét (float), hoặc `None` nếu dòng bị lỗi.
#
# Ví dụ:
#
# | Lời gọi | Kết quả |
# |---|---|
# | `doc_khoang_cach("113.05,694.5\n")` | `6.945` |
# | `doc_khoang_cach("9.75,\n")` | `None` |
# | `doc_khoang_cach("6.70,0.0\n")` | `None` |
# | `doc_khoang_cach("5.00,1200.0\n")` | `12.0` |
#
# Bộ chấm gọi hàm với bốn loại dòng trên, có dòng không kết thúc bằng `\n`.

# %%
def doc_khoang_cach(dong):
    # TODO: tách dòng, kiểm tra ô khoảng cách, đổi cm sang m, kết thúc bằng return
    pass  # Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_4_3(doc_khoang_cach)

# %% [markdown]
# ### 📡 Bài tập 4.4 — Hàm đổi toạ độ
#
# Toạ độ trong `data/gps.nmea` có dạng `ddmm.mmmmm` (vĩ độ) hoặc `dddmm.mmmmm` (kinh
# độ), hướng `N`, `S`, `E`, `W` nằm ở ô kế bên. Gọi $x$ là chuỗi toạ độ đã ép sang
# số:
#
# $$\text{do} = \left\lfloor \frac{x}{100} \right\rfloor, \qquad \text{phut} = x \bmod 100, \qquad \theta = \text{do} + \frac{\text{phut}}{60}$$
#
# Viết hàm `nmea_sang_do(chuoi, huong)` trả về độ thập phân $\theta$. Hướng `"S"` và `"W"` thì
# trả về số âm. Chuỗi rỗng (lúc mất fix GPS, ô toạ độ để trống) thì trả về `None`.
#
# Ví dụ:
#
# | Lời gọi | Kết quả |
# |---|---|
# | `nmea_sang_do("2103.00000", "N")` | `21.05` |
# | `nmea_sang_do("10603.00000", "W")` | `-106.05` |
# | `nmea_sang_do("", "N")` | `None` |

# %%
def nmea_sang_do(chuoi, huong):
    # TODO: đổi sang độ thập phân, xét hướng, kết thúc bằng return
    pass  # Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_4_4(nmea_sang_do)

# %% [markdown]
# ---
# ## Bài 5 — Vòng lặp và đọc file
#
# #### 📖 Cú pháp
#
# | Cú pháp | Nghĩa | Ví dụ |
# |---|---|---|
# | `for x in day:` | lặp lại khối lệnh thụt lề bên dưới, mỗi vòng `x` nhận một giá trị của `day` (dãy giá trị) | `for i in range(3):` |
# | `range(n)` | dãy số nguyên từ `0` đến `n - 1` | `range(3)` → `0, 1, 2` |
# | `range(a, b, buoc)` | dãy số từ `a` đến trước `b`, mỗi số cách số trước `buoc` | `range(2, 10, 3)` → `2, 5, 8` |
# | `while dieu_kien:` | lặp khi điều kiện còn đúng, kiểm tra lại trước mỗi vòng | `while v > 0:` |
# | `break` | thoát hẳn khỏi vòng lặp | `if ax < -5.0: break` |
# | `continue` | bỏ phần còn lại của vòng hiện tại, sang vòng kế tiếp | `if o == "": continue` |
# | `tong += x` | cộng dồn, giống `tong = tong + x` | `tong += 2.5` |
# | `dem += 1` | đếm, tăng `dem` lên 1 | `dem += 1` |
# | `v -= a` | trừ dồn, giống `v = v - a` | `v -= 0.5` |
# | `import ten_module` | nạp một module (thư viện) có sẵn, gọi hàm bằng `ten_module.ten_ham` | `import math`, rồi `math.sqrt(16)` → `4.0` |
# | `from ten_module import ten_ham` | nạp riêng `ten_ham` từ module, gọi thẳng bằng tên | `from math import sqrt`, rồi `sqrt(16)` → `4.0` |
# | `with open(duong_dan) as f:` | mở file để đọc, ra khỏi khối `with` thì file tự đóng | `with open("data/obd.csv") as f:` |
# | `for dong in f:` | duyệt từng dòng của file, mỗi `dong` là một chuỗi kết thúc bằng `\n` | `for dong in f:` |
# | `next(f)` | đọc và bỏ qua một dòng, dùng để bỏ dòng tiêu đề | `next(f)` |
# | `csv.DictReader(f)` | đọc file `.csv`, mỗi vòng cho một hàng, tên cột lấy từ dòng tiêu đề (cần `import csv`) | `for hang in csv.DictReader(f):` |
# | `hang["ten_cot"]` | lấy giá trị của cột `ten_cot` trong hàng, luôn là chuỗi | `hang["toc_do_kmh"]` → `"40"` |
# | `dong.startswith("$GNGGA")` | `True` nếu dòng bắt đầu bằng chuỗi đó | `"$GNGGA,1".startswith("$GNGGA")` → `True` |
#
# #### ⚠️ Lỗi hay gặp
#
# - Mọi thứ đọc từ file đều là chuỗi `str`: `hang["toc_do_kmh"]` là `"40"`. Phải ép
#   `int()` hoặc `float()` trước khi so sánh hay cộng.
# - Quên bỏ dòng tiêu đề khi duyệt file bằng `for dong in f:`. Dòng đầu là chữ, ép kiểu
#   sẽ báo `ValueError`. Thêm `next(f)` trước vòng lặp. `csv.DictReader` tự bỏ dòng
#   tiêu đề.
# - Đặt biến đếm bên trong vòng lặp: mỗi vòng biến về 0 lại từ đầu. Đặt `dem = 0` trước
#   vòng lặp.
# - `while` mà điều kiện không bao giờ sai thì chạy mãi. Trong thân vòng lặp phải có
#   dòng làm điều kiện tiến dần tới sai, và bấm Interrupt để dừng nếu lỡ viết sai.

# %%
# 💻 Ví dụ: for với range
for i in range(3):          # i lần lượt là 0, 1, 2
    print("vong", i)

# %%
# 💻 Ví dụ: cộng dồn và đếm
tong = 0
dem = 0
for toc_do in range(10, 60, 10):   # 10, 20, 30, 40, 50
    tong += toc_do
    dem += 1
print(tong / dem)

# %% [markdown]
# `tong` và `dem` được đặt về 0 trước vòng lặp, rồi mới cộng dồn.

# %%
# 💻 Ví dụ: continue
for so in range(1, 8):
    if so % 2 == 0:
        continue        # số chẵn: bỏ qua, sang vòng kế tiếp
    print(so)

# %%
# 💻 Ví dụ: break
for so in range(1, 10):
    if so * so > 20:
        print(so)       # số đầu tiên có bình phương lớn hơn 20
        break           # thoát hẳn, không xét các số sau

# %%
# 💻 Ví dụ: while
v = 10.0
while v > 0:
    v -= 3              # 7.0, 4.0, 1.0, -2.0 rồi dừng
print(v)

# %%
# 💻 Ví dụ: import và from ... import
import math                     # nạp cả module math
from math import sqrt           # nạp riêng hàm sqrt

print(math.pi, math.sqrt(16))   # dùng qua tên module
print(sqrt(16))                 # dùng thẳng tên hàm

# %% [markdown]
# Ô thiết lập ở đầu notebook dùng đúng cú pháp `from ... import` này để lấy các hàm
# `kiem_tra_*` về.

# %%
# 💻 Ví dụ: đọc obd.csv bằng csv.DictReader
import csv

with open("data/obd.csv") as f:
    for hang in csv.DictReader(f):
        if float(hang["thoi_gian_s"]) > 2:    # hang[...] là chuỗi, phải ép float
            break
        print(hang["thoi_gian_s"], hang["rpm"])

# %%
# 💻 Ví dụ: đếm số câu $GNGGA trong gps.nmea
dem_gga = 0
with open("data/gps.nmea") as f:
    for dong in f:
        if dong.startswith("$GNGGA"):
            dem_gga += 1
print(dem_gga)

# %% [markdown]
# ### 📡 Bài tập 5.1 — Đếm mẫu LiDAR hợp lệ
#
# Đọc `data/khoang_cach_truoc.csv` (LiDAR 1D, 20 mẫu mỗi giây, cả chuyến 180 giây) bằng
# `open` và `for`. Dòng nào mà `doc_khoang_cach` trả về `None` (mất tín hiệu hoặc ô
# trống) là dòng lỗi, các dòng còn lại là hợp lệ.
#
# Gán `so_mau_hop_le` và `so_mau_loi`.
#
# Ví dụ: file chỉ có 5 dòng dữ liệu `1.00,320.5`, `1.05,0.0`, `1.10,318.0`, `1.15,`,
# `1.20,317.2` cho `so_mau_hop_le = 3`, `so_mau_loi = 2`.

# %%
so_mau_hop_le = None  # TODO
so_mau_loi = None     # TODO

# Viết vòng lặp của bạn vào ngay dưới dòng này. Khung cú pháp:
# with open("data/khoang_cach_truoc.csv") as f:
#     next(f)
#     for dong in f:
#         ...


# %%
kiem_tra_5_1(so_mau_hop_le, so_mau_loi)

# %% [markdown]
# ### 📡 Bài tập 5.2 — Thống kê tốc độ OBD
#
# Đọc `data/obd.csv` (tốc độ xe qua OBD-II, 1 mẫu mỗi giây) bằng `csv.DictReader`. Cột
# tốc độ là `toc_do_kmh`.
#
# Gán `toc_do_max` (tốc độ lớn nhất) và `toc_do_tb` (trung bình của mọi mẫu).
#
# Ví dụ: ba mẫu có tốc độ `0`, `40`, `65` cho `toc_do_max = 65`, `toc_do_tb = 35.0`.

# %%
toc_do_max = None  # TODO
toc_do_tb = None   # TODO

# Viết code đọc file của bạn vào ngay dưới dòng này. Khung cú pháp:
# import csv
# with open("data/obd.csv") as f:
#     for hang in csv.DictReader(f):
#         ...


# %%
kiem_tra_5_2(toc_do_max, toc_do_tb)

# %% [markdown]
# ### 📡 Bài tập 5.3 — Tìm thời điểm phanh gấp
#
# Đọc `data/imu.csv` (IMU 6 trục, 50 mẫu mỗi giây). Cột `ax` là gia tốc dọc xe, âm khi
# phanh. Tìm thời điểm `thoi_gian_s` đầu tiên có `ax` nhỏ hơn `-5.0`, rồi dừng vòng
# lặp ngay.
#
# Gán `t_phanh_gap` (float, giây).
#
# Ví dụ: `ax` lần lượt là `0.1`, `-2.0`, `-5.5`, `-7.0` tại các giây `1.00`, `1.02`,
# `1.04`, `1.06` cho `t_phanh_gap = 1.04`.

# %%
t_phanh_gap = None  # TODO

# Viết code đọc file của bạn vào ngay dưới dòng này:


# %%
kiem_tra_5_3(t_phanh_gap)

# %% [markdown]
# ### 📡 Bài tập 5.4 — Đếm số giây RTK fixed
#
# Đọc `data/gps.nmea`. File có hai loại câu, `$GNRMC` và `$GNGGA`, bỏ qua câu không
# phải `$GNGGA`. Mã fix nằm ở cột 6 của câu `$GNGGA` (đếm từ 0 sau khi cắt theo dấu
# phẩy), mã `4` là RTK fixed. Mỗi câu `$GNGGA` ứng với 1 giây.
#
# Gán `so_giay_rtk_fixed` (int).
#
# Ví dụ: ba câu `$GNGGA` có mã fix `4`, `5`, `4` cho `so_giay_rtk_fixed = 2`.

# %%
so_giay_rtk_fixed = None  # TODO

# Viết code đọc file của bạn vào ngay dưới dòng này:


# %%
kiem_tra_5_4(so_giay_rtk_fixed)

# %% [markdown]
# ### 📡 Bài tập 5.5 — Quãng đường phanh
#
# Xe đang chạy với tốc độ `v0_kmh` (km/h) thì phanh với gia tốc không đổi `gia_toc`
# (m/s²). Mô phỏng theo từng bước thời gian `dt` (giây): mỗi bước vận tốc giảm
# $a \cdot \Delta t$ và xe đi thêm $v \cdot \Delta t$, lặp cho tới khi vận tốc không
# còn dương. Đổi tốc độ sang m/s trước khi mô phỏng:
#
# $$v\,[\text{m/s}] = \frac{v\,[\text{km/h}]}{3.6}$$
#
# Viết hàm `quang_duong_phanh(v0_kmh, gia_toc, dt)` trả về tổng quãng đường (mét). Kết
# quả sát với $\dfrac{v_0^2}{2a}$ ($v_0$ tính bằng m/s), bộ chấm chấp nhận sai lệch tối
# đa $v_0 \cdot \Delta t$.
#
# Ví dụ: `quang_duong_phanh(72, 5.0, 0.01)` cho khoảng `40` m.
# `quang_duong_phanh(0, 5.0, 0.01)` cho `0`.

# %%
def quang_duong_phanh(v0_kmh, gia_toc, dt):
    # TODO: vòng lặp while mô phỏng từng bước, kết thúc bằng return
    pass  # Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_5_5(quang_duong_phanh)

# %% [markdown]
# ---
# ## Dự án tuần 1 — Bộ ra quyết định lái xe trên một chuyến xe
#
# Dự án ghép dữ liệu của ba cảm biến trên cùng một chuyến xe dài 180 giây: LiDAR đo
# khoảng cách phía trước, OBD cho tốc độ và mức pin, GPS cho quỹ đạo. Phần 1 viết hàm
# quyết định. Phần 2 chạy hàm đó qua từng giây của chuyến.
#
# #### Phần 1 — Hàm quyết định
#
# Viết hàm `quyet_dinh_lai_xe(khoang_cach, toc_do, muc_pin)` trả về một trong bốn
# mã lệnh, xét theo đúng thứ tự ưu tiên sau:
#
# 1. `khoang_cach <= 2.0` → `"DUNG_KHAN_CAP"`
# 2. `muc_pin < 15` → `"VE_TRAM_SAC"`
# 3. `khoang_cach <= 5.0` hoặc `toc_do > 60` → `"GIAM_TOC"`
# 4. còn lại → `"BINH_THUONG"`
#
# Thứ tự này là một phần của đề bài. An toàn xét trước năng lượng: xe sắp hết pin
# nhưng có vật cản ngay trước mặt thì vẫn phải dừng khẩn cấp. Viết `elif` theo đúng
# thứ tự trên là tự khắc đúng.
#
# Điều kiện 3 cần `or`, vì chỉ cần một trong hai vế đúng là đủ.

# %%
def quyet_dinh_lai_xe(khoang_cach, toc_do, muc_pin):
    # TODO: if/elif/else theo đúng 4 mức ưu tiên trên, kết thúc bằng return
    pass  #Bỏ pass khi hoàn thiện hàm


# %%
kiem_tra_du_an(quyet_dinh_lai_xe)

# %% [markdown]
# #### Phần 2 — Chạy trên cả chuyến xe
#
# `doc_chuyen_xe()` được viết sẵn. Nó đọc `khoang_cach_truoc.csv` và `obd.csv`, ghép về
# mỗi giây một bộ bốn giá trị:
#
# | Giá trị | Nghĩa |
# |---|---|
# | `t` | thời điểm, giây |
# | `khoang_cach` | khoảng cách phía trước (m), là trung vị các mẫu LiDAR hợp lệ trong giây đó, `None` nếu giây đó không có mẫu hợp lệ |
# | `toc_do` | tốc độ (km/h) |
# | `pin` | mức pin (%) |
#
# Cú pháp lấy bốn giá trị cùng lúc, mỗi vòng gán lần lượt vào bốn tên:
#
# ```python
# for t, khoang_cach, toc_do, pin in doc_chuyen_xe():
#     ...
# ```
#
# Với mỗi giây có `khoang_cach` (bỏ qua giây `None`), gọi `quyet_dinh_lai_xe`, đếm số
# giây của từng lệnh và ghi lại thời điểm `DUNG_KHAN_CAP` đầu tiên. Gán
# `so_lan_dung`, `so_lan_ve_sac`, `so_lan_giam_toc`, `so_lan_binh_thuong` (int) và
# `t_dung_dau_tien` (int, giây).
#
# Ví dụ: ba giây `(0, 12.0, 0, 15.8)`, `(1, None, 0, 15.8)`, `(2, 1.5, 0, 15.8)` cho
# `so_lan_binh_thuong = 1`, `so_lan_dung = 1`, `t_dung_dau_tien = 2`. Giây 1 bị bỏ
# qua vì `khoang_cach` là `None`.

# %%
from tests.tien_ich_du_lieu import doc_chuyen_xe, ve_chuyen_xe

so_lan_dung = None
so_lan_ve_sac = None
so_lan_giam_toc = None
so_lan_binh_thuong = None
t_dung_dau_tien = None

# Viết vòng lặp của bạn vào ngay dưới dòng này. Khung cú pháp:
# for t, khoang_cach, toc_do, pin in doc_chuyen_xe():
#     ...


# %%
kiem_tra_lab(so_lan_dung, so_lan_ve_sac, so_lan_giam_toc, so_lan_binh_thuong, t_dung_dau_tien)

# %% [markdown]
# Vẽ lại cả chuyến xe, màu theo lệnh mà hàm `quyet_dinh_lai_xe` của bạn chọn.

# %%
ve_chuyen_xe(quyet_dinh_lai_xe)

# %% [markdown]
# ### Xem trước: pandas
#
# Đọc file `.csv` rồi thống kê tốc độ bằng thư viện `pandas` chỉ cần vài dòng.

# %%
# 💻 Ví dụ: pandas
import pandas as pd

df = pd.read_csv("data/obd.csv")                  # đọc cả file thành một bảng
print(df.describe())                              # thống kê mô tả của từng cột
df.plot(x="thoi_gian_s", y="toc_do_kmh")          # vẽ tốc độ theo thời gian

# %% [markdown]
# ---
# ## Tổng kết tuần 1
#
# Chạy ô dưới để kiểm tra toàn bộ bài trong tuần.

# %%
ket_qua = [
    kiem_tra_1_1(tb_doc_1, tb_doc_2),
    kiem_tra_1_2(noi_chuoi, tong_so),
    kiem_tra_1_3(thoi_gian_mau, khoang_cach_m),
    kiem_tra_2_1(moi_xe_tra_1, moi_xe_tra_2),
    kiem_tra_2_2(bao_cao),
    kiem_tra_2_3(gio, phut, giay),
    kiem_tra_2_4(vi_do),
    kiem_tra_2_5(gio_vn, phut_vn, giay_vn),
    kiem_tra_3_1(trang_thai),
    kiem_tra_3_2(gioi_han),
    kiem_tra_3_3(trang_thai_fix_1, trang_thai_fix_2, trang_thai_fix_3),
    kiem_tra_4_1(canh_bao_vat_can),
    kiem_tra_4_2(gioi_han_toc_do),
    kiem_tra_4_3(doc_khoang_cach),
    kiem_tra_4_4(nmea_sang_do),
    kiem_tra_5_1(so_mau_hop_le, so_mau_loi),
    kiem_tra_5_2(toc_do_max, toc_do_tb),
    kiem_tra_5_3(t_phanh_gap),
    kiem_tra_5_4(so_giay_rtk_fixed),
    kiem_tra_5_5(quang_duong_phanh),
    kiem_tra_du_an(quyet_dinh_lai_xe),
    kiem_tra_lab(so_lan_dung, so_lan_ve_sac, so_lan_giam_toc, so_lan_binh_thuong, t_dung_dau_tien),
]

print(f"\nTONG KET TUAN 1: {sum(ket_qua)}/{len(ket_qua)} bai dat.")

# %% [markdown]
# ### Lưu bài
#
# Vào `File > Save a copy in Drive` để giữ lại bài đã làm. Đóng tab khi chưa lưu thì bài
# làm trong phiên này mất.
