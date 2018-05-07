fopen = open("words.txt", "r")
fread = fopen.read()
for i in fread:
    if len(i) > 0:
        print(i)
