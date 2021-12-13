l = 2
r = 2
for i in range(5):
	for j in range(5):
		if(i % 2 == 0):
			if(j>=l) and (j<=r):
				print(" ",end="*")
			else:
				print(" ",end=" ")
		else:
			if(j>=l+1) and (j<=r):
				print("*",end=" ")
			else:
				print(" ",end=" ")
	print()
	if(i % 2 == 0):
		l -= 1
		r += 1
