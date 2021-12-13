def sub(x,t):
	hasil = []
	for i in range(len(x)-1):
		for j in range(i+1,len(x)):
			if(x[i]+x[j]==t):
				hasil.append([i, j])
	return hasil

a = map(int,input("Input daftar angka dipisah \", \" tanpa kurung siku: ").split(", "))
b = list(a)
c = int(input("Input Target jumlah yang diinginkan: "))
print("Indeks pasangan bilangan yang dijumlahkan akan memiliki hasil yang sama dengan",c,"adalah: ",sub(b,c))
