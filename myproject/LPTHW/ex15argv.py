from sys import argv
# su dung argv de truyen tham so vao chuong trinh tu commanline

script,filename = argv

# truyen bien tu commanline cho script va filename
# script va filename co dang list
# script va filename nhan gia tri theo thu tu bien duoc truyen vao
# argv mac dinh ten chuong trinh se duoc truyen truoc tien => script = ten chuong trinh

txt = open(filename)
# filename = "tenbien"

print("Here's you name of program %s" %script)
print("Here's you file %r" %filename)
print("and here's filename list u have input from commanline: %s %r"%(script,filename))
print(txt.read())
#filename[0] = "ex15.py"
#filename[1] = "tenbien"

print("Type the filename again: \n")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

