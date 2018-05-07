#vd truyen nhieu bien argv vao 1 bien
from sys import argv

script = argv
# Mac dinh ten chuong trinh se duoc tu dong truyen vao truoc tien

for i in script:
	print(script.index(i),i,end="\n")
	# script.index(i) : xac dinh index cua i trong list script
	# end="\n" : xuong dong sau moi gia tri i
