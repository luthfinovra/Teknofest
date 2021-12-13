def banyak(x):
	c = {}
	for i in x:
		if(i not in c.keys()):
			c[i] = 1
		else:
			c[i] += 1
	return c
a = input("input karakter-karakter tanpa tanda kutip \ndipisahkan oleh \", \" tanpa kurung siku : ").split(", ")
z = list(a)
b = banyak(z)
print("karakter-karakter yang telah diinput muncul sebanyak:")
b = dict(sorted(b.items(), key=lambda x:x[1]))
for i in b:
	print(i+":",b[i])
