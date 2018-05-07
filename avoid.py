def avoids():
    # nhap modun re de goi ham re.sub()
    import re
    # Khoi tao blacklist
    blacklist = []
    list_blackwords = []
    list_whitewords = []
    while True:
        words = input("Nhap danh sach ca tu khong duoc dung. end de ket thuc: \n")
        if words != "end":
            blacklist.append(words)
        # end dung de ket thuc vong lap khoi tao blacklist
        elif words == "end":
            break
    print("Danh sach cac tu bi cam dung: \n", blacklist)

    # Khoi tao tu nhap vao boi user
    string = input("Nhap tu cua ban: \n")
    # Xoa cac ky tu dac biet ra khoi string
    string = re.sub("[/\W]"," ",string)
    list_of_string = string.split()

    # Kiem tra
    for words in list_of_string:
        if words in blacklist:
            # Tao danh sach blackword
            list_blackwords.append(words)
        else:
            list_whitewords.append(words)
    if list_blackwords != []:
        print("Tu ** %s ** khong hop le!!.\nCo chua cac ky tu cam: %s.\nCac tu khong chua ky tu cam: %s"%(string,list_blackwords,list_whitewords))
    elif list_blackwords == []:
        print("Tu %s Hop le"%string)
avoids()