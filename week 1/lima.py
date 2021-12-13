l = 0
r = 4
for i in range(5):
	for j in range(5):
		if(i % 2 == 0):
			if(j>=l) and (j<=r):
				print(" ",end="*")
			else:
				print(" ",end=" ")
		else:
			if(j>=l) and (j<=r+1):
				print("*",end=" ")
			else:
				print(" ",end=" ")
	print()
	if(i % 2 == 0):
		l += 1
		r -= 1
