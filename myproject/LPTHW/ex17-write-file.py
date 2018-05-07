##Chuong trinh tao file
from sys import argv
from os.path import exists


scriptName, ex17File = argv

print("Does file is exist !! %r"%exists(ex17File))
#Kiem tra su ton tai cua file
print("Press eny key to continues. Press Ctr + C to quit!");input("");number = input("Please input number: \n")

writeFile = open(ex17File,"w")
for i in range(int(number)):
	writeFile.write(str(i)+" ")
	
print("All thing done! Do u want read %s again? If yes, press enter. If not, press Ctr + C \n"%ex17File)
input("")
print("This's you file affter: \n")
writeFile = open(ex17File,"r")
readFile = writeFile.read()
print(readFile)
print("%d byte len long"%len(readFile))

writeFile.close()