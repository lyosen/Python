fopen = open('thinkpython/words.txt',"r")
fread = fopen.read()
for i in fread:
    print(i)
