# - *- coding: utf- 8 - *-
def is_sorted():
    """Hàm kiểm tra danh sach ky tu da được sắp xếp chưa"""
    j = 1
    a = input("Nhap danh sach ky tu: \n")
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            j += 1
        elif a[i] > a[i + 1]:
            break
    if j == len(a):
        print("True")
    elif j < len(a):
        print("False")
is_sorted()