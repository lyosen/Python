def check_ferman(a,b,c,n):	
	if n < 2:
		print("%d phai lon hon 2"%n)
	elif n > 2:
		for a in range(1000):
			for b in range(1000):
				for c in range(1000):
					if a ** n + b ** n == c ** n:
						return False
		else:
			print("Ferman i right")
check = check_ferman(1,2,3,1)
print (check)
if check == False:
	print("Ferman is wrong")
else:
	print("ferman is right")
