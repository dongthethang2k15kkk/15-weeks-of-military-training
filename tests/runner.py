"""Bộ máy chấm bài dùng chung cho khoá AI Course v2 (BK-AUTO).

Dùng ở 2 nơi với cùng một bộ test:
  - Trong Colab: học viên bấm Run, nhận kết quả PASS/FAIL.
  - Trong GitHub Actions: đặt biến môi trường AUTOGRADE=1 -> sai thì báo lỗi,
    workflow tự đánh trượt bài nộp.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass, field
from typing import Any

# Khi chạy tự động trên GitHub Actions thì sai phải văng lỗi, không chỉ in ra.
STRICT = os.environ.get("AUTOGRADE") == "1"

XANH, DO, VANG, XAM, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[90m", "\033[0m"


@dataclass
class Case:
    """Một trường hợp kiểm thử.

    args     : tham số truyền vào hàm
    kwargs   : tham số dạng từ khoá
    expected : giá trị mong đợi hàm trả về
    raises   : loại lỗi mong đợi hàm phải ném ra (dùng thay cho expected)
    mo_ta    : mô tả ngắn hiển thị cho học viên
    """

    args: tuple = ()
    kwargs: dict = field(default_factory=dict)
    expected: Any = None
    raises: type | None = None
    mo_ta: str = ""


def _giong_nhau(thuc_te: Any, mong_doi: Any, sai_so: float = 1e-6) -> bool:
    """So sánh kết quả, có dung sai cho số thực."""
    if isinstance(mong_doi, bool) or isinstance(thuc_te, bool):
        return thuc_te is mong_doi
    if isinstance(mong_doi, (int, float)) and isinstance(thuc_te, (int, float)):
        return math.isclose(float(thuc_te), float(mong_doi), rel_tol=sai_so, abs_tol=sai_so)
    return thuc_te == mong_doi


def _rut_gon(gia_tri: Any, n: int = 70) -> str:
    s = repr(gia_tri)
    return s if len(s) <= n else s[: n - 3] + "..."


def _nhan(ham, c: Case) -> str:
    if c.mo_ta:
        return c.mo_ta
    phan = [_rut_gon(a, 25) for a in c.args]
    phan += [f"{k}={_rut_gon(v, 25)}" for k, v in c.kwargs.items()]
    return f"{getattr(ham, '__name__', 'ham')}({', '.join(phan)})"


def kiem_tra(ten_bai: str, ham: Any, cases: list[Case], sai_so: float = 1e-6) -> bool:
    """Chạy toàn bộ test case cho một bài tập và in kết quả."""
    print(f"\n{ten_bai}")

    if not callable(ham):
        print(f"  {DO}FAIL  Chưa tìm thấy hàm cần kiểm tra."
              f" Bạn đã xoá dòng TODO và định nghĩa hàm chưa?{RESET}")
        if STRICT:
            raise AssertionError(f"{ten_bai}: chưa có hàm để chấm")
        return False

    dat = 0
    for i, c in enumerate(cases, 1):
        nhan = _nhan(ham, c)
        try:
            ket_qua = ham(*c.args, **c.kwargs)
        except Exception as loi:  # noqa: BLE001 - cần bắt mọi lỗi của học viên
            if c.raises is not None and isinstance(loi, c.raises):
                dat += 1
                print(f"  {XANH}PASS  test {i}{RESET}: {nhan} -> ném {type(loi).__name__} (đúng như mong đợi)")
            else:
                mong = f"ném {c.raises.__name__}" if c.raises else _rut_gon(c.expected)
                print(f"  {DO}FAIL  test {i}{RESET}: {nhan}")
                print(f"     {XAM}mong đợi:{RESET} {mong}")
                print(f"     {XAM}thực tế :{RESET} chương trình lỗi {type(loi).__name__}: {loi}")
            continue

        if c.raises is not None:
            print(f"  {DO}FAIL  test {i}{RESET}: {nhan}")
            print(f"     {XAM}mong đợi:{RESET} ném {c.raises.__name__} khi dữ liệu không hợp lệ")
            print(f"     {XAM}thực tế :{RESET} trả về {_rut_gon(ket_qua)}")
        elif _giong_nhau(ket_qua, c.expected, sai_so):
            dat += 1
            print(f"  {XANH}PASS  test {i}{RESET}: {nhan} -> {_rut_gon(ket_qua)}")
        else:
            print(f"  {DO}FAIL  test {i}{RESET}: {nhan}")
            print(f"     {XAM}mong đợi:{RESET} {_rut_gon(c.expected)}")
            print(f"     {XAM}thực tế :{RESET} {_rut_gon(ket_qua)}")

    tong = len(cases)
    if dat == tong:
        print(f"  {XANH}Kết quả: {dat}/{tong} — Đạt!{RESET}")
    else:
        print(f"  {VANG}Kết quả: {dat}/{tong} — Xem lại các test còn đỏ rồi chạy lại ô này nhé.{RESET}")

    if STRICT and dat < tong:
        raise AssertionError(f"{ten_bai}: {dat}/{tong} test đạt")
    return dat == tong


def kiem_tra_gia_tri(ten_bai: str, cap: list[tuple[str, Any, Any]], sai_so: float = 1e-6) -> bool:
    """Chấm bài không dùng hàm: so sánh giá trị biến học viên đã gán.

    cap: danh sách (nhãn hiển thị, giá trị thực tế, giá trị mong đợi).
    Dùng cho các tuần chưa dạy `def` — học viên gán thẳng biến thay vì viết hàm.
    """
    print(f"\n{ten_bai}")

    dat = 0
    for i, (nhan, thuc_te, mong_doi) in enumerate(cap, 1):
        if thuc_te is None:
            print(f"  {DO}FAIL  test {i}{RESET}: {nhan}")
            print(f"     {XAM}mong đợi:{RESET} {_rut_gon(mong_doi)}")
            print(f"     {XAM}thực tế :{RESET} biến chưa được gán, vẫn còn là None")
        elif _giong_nhau(thuc_te, mong_doi, sai_so):
            dat += 1
            print(f"  {XANH}PASS  test {i}{RESET}: {nhan} -> {_rut_gon(thuc_te)}")
        else:
            print(f"  {DO}FAIL  test {i}{RESET}: {nhan}")
            print(f"     {XAM}mong đợi:{RESET} {_rut_gon(mong_doi)}")
            print(f"     {XAM}thực tế :{RESET} {_rut_gon(thuc_te)}")

    tong = len(cap)
    if dat == tong:
        print(f"  {XANH}Kết quả: {dat}/{tong} — Đạt!{RESET}")
    else:
        print(f"  {VANG}Kết quả: {dat}/{tong} — Xem lại các test còn đỏ rồi chạy lại ô này nhé.{RESET}")

    if STRICT and dat < tong:
        raise AssertionError(f"{ten_bai}: {dat}/{tong} test đạt")
    return dat == tong