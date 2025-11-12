a1 = (2, 0, 5)
a2 = (1, 9, 6, 5)

a_gabung = a1 + a2

angka = []
for i in a_gabung:
    ada = False
    for u in angka:
        if i == u:
            ada = True
            break
    if not ada:
        angka.append(i)

n = 0
for _ in angka:    
    n += 1

for i in range(n):
    for j in range(n - 1):
        if angka[j] < angka[j + 1]:
       
            temp = angka[j]
            angka[j] = angka[j + 1]
            angka[j + 1] = temp


hasil = ()
for x in angka:
    hasil += (x,)

print("Berikut angka dari terbesar", hasil)