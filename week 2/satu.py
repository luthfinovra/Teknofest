def satukali(x):
	b = {}
	hasil = []
	memo = ""
	for i in x:
		if(i not in memo):
			memo += i
			b[i] = 1
		else:
			b[i] += 1
	for i in b.keys():
		if(b[i]==1):
			hasil.append(int(i))
	return hasil


a = input("Input angka tanpa tanda kutip: ")
print("angka yang muncul sekali: ",satukali(a))
