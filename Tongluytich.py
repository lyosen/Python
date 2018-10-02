
def Cumulative_total():
    """Chuong trinh tinh Tong luy tich cua mot day so"""
    t = input("Nhap vao mot day danh sach cac so theo cuu phap 12549... \n")
    t1 = []
    t2 = []
    j = 0

    """Duyet tung gia tri cua t => int roi them vao danh sach t1"""
    for x in t:
        t1.append(int(x))

    """Duyet tung phan tu trong danh sach t1 va thuc hien tinh tong cua luy thua [1,2,3] ==> [1,3,6]"""
    for i in t1:
        j += i
        t2.append(j)
    print(t1)
    print("\n")
    print(t2)
Cumulative_total()


