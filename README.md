# 15 tuần khổ luyện — AI for Automobile (BK-AUTO)

Khoá Python và AI — AI for Automobile (BK-AUTO)

| Tuần | Chủ đề | Mở trên Colab |
|---|---|---|
| 1 | Nền tảng, cú pháp cơ bản, vòng lặp và đọc file log cảm biến | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dongthethang2k15kkk/15-weeks-of-military-training/blob/main/week1/week_1.ipynb) |

Các tuần sau được thêm vào bảng khi đến tuần đó.

## Cách học

1. Bấm nút "Open in Colab" của tuần hiện tại (cần đăng nhập Google).
2. Chạy ô đầu tiên. Ô này tự tải các file của tuần đó về máy ảo Colab, không cần cài gì thêm.
3. Đọc bảng cú pháp, chạy các ô ví dụ, rồi làm bài tập. Mỗi bài tập có một ô kiểm tra ngay bên dưới.
4. Vào `File > Save a copy in Drive` để giữ bản nháp. Đóng tab khi chưa lưu thì bài làm trong phiên đó mất.

Mỗi tuần chỉ cần mở một notebook. Học tuần mới không phải tải lại file của tuần cũ.

## Nộp bài

1. Tạo repo của bạn từ template, chỉ làm một lần: bấm [Use this template](https://github.com/dongthethang2k15kkk/15-weeks-of-military-training/generate), đặt tên repo, chọn **Private**.
2. Làm bài trên Colab. Khi xong, vào `File > Save a copy in GitHub`, chọn repo của bạn, đường dẫn đúng thư mục của tuần (ví dụ `week1/week_1.ipynb`), ghi commit message dạng `week1: hoan thanh bai tap`. Lần lưu đầu Colab hỏi quyền truy cập GitHub, chọn cho phép.
3. Mở tab **Actions** của repo. GitHub chạy lại notebook của bạn và chấm: dấu xanh là mọi bài đạt, dấu đỏ là còn bài sai, bấm vào để xem bài nào.

## Dữ liệu

Thư mục [data/](data/) là dữ liệu **mô phỏng** của một chuyến xe dài 180 giây, gồm bốn loại cảm biến: LiDAR đo khoảng cách phía trước, GPS (NMEA), OBD-II và IMU. Mô tả từng cột nằm trong [data/README.md](data/README.md).

## Cấu trúc repo

```
weekN/        notebook của từng tuần
tests/        bộ chấm bài: runner.py dùng chung, test_weekN.py của từng tuần,
              tien_ich_du_lieu.py (hàm đọc và vẽ dữ liệu chuyến xe)
data/         dữ liệu cảm biến
assets/       hình dùng trong notebook
src/          nguồn .py của notebook (jupytext)
tools/        script sinh dữ liệu
```