#mengganti Nilai List
# buah = ["jeruk", "apel","mangga","duren"]
# buah[2]="kelapa"
# print(buah)

#menambahkan index di list(Metode Append)
# buah = ["jeruk", "apel", "mangga", "duren"]
# buah.append("anggur")
#print(buah)

#Metode insert
# buah = ["jeruk", "apel", "mangga", "duren"]
# buah.insert(2,"anggur")
# print(buah)

# #menghapus Item dilist
# buah = ["jeruk", "apel", "mangga", "duren"]
# del buah [1]
# print(buah)

# abjad = ["a","b","c","d"]
# abjad.remove("c")
# print(abjad)

#memotong list
# warna = ["merah","hijau","kuning","biru","pink","ungu"]
# print(warna[1:4])


#operasi list
#penggabunga(+)
#perkalian(*)

#contoh penggabungan
# list_lagu = ["No Women, No Cry","Dear God"]
# playlist_favorit = ["Break Out","Now Loading!!!"]
# semua_lagu = list_lagu + playlist_favorit
# print(semua_lagu)

#contoh perkalian
# playlist_favorit = ["Break Out","Now Loading!!!"]
# ulangi = 3
 
# now_playlist = playlist_favorit * ulangi
# print(now_playlist)

# bulan = [""] * (5)

# for i in range(0, 4 + 1, 1):
#     bulan[i] = input("Masukan Nilai i : ")
# for i in range(0, 4 + 1, 1):
    
#     print("[", bulan[i], "] ", end="")


# A = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [7, 9, 11]
# ]

# B = [
#     [1, 2, 3],
#     [3, 2, 1],
#     [4, 5, 6]
# ]

# print("Matriks A:")
# for baris in A:
#     print(baris)

# print("\nMatriks B:")
# for baris in B:
#     print(baris)

# hasil = []
# for i in range(len(A)):              # Loop baris
#     baris = []
#     for j in range(len(A[0])):       # Loop kolom
#         baris.append(A[i][j] + B[i][j])
#     hasil.append(baris)

# # Menampilkan hasil penjumlahan
# print("\nHasil Penjumlahan Matriks (A + B):")
# for baris in hasil:
#     print(baris)

# Penjumlahan
# mat1 = [
#     [5, 0],
#     [2, 6],
# ]
# mat2 = [
#     [1, 0],
#     [4, 2],
# ]
# for x in range(0, len(mat1)):
#     for y in range(0, len(mat1[0])):
#         print (mat1[x][y] + mat2[x][y], end=' '),
#     print()

# # Pengurangan
# mat1 = [
#     [5, 0],
#     [2, 6],
# ]
# mat2 = [
#     [1, 0],
#     [4, 2],
# ]
# for x in range(0, len(mat1)):
#     for y in range(0, len(mat1[0])):
#         print (mat1[x][y] - mat2[x][y], end=' '),
#     print()

# Perkalian
# mat1 = [
#     [5, 0],
#     [2, 6],
# ]
# mat2 = [
#     [1, 0],
#     [4, 2],
# ]
# mat3 = [ ]
# for x in range(0, len(mat1)):
#     row = [ ]
#     for y in range(0, len(mat1[0])):
#         total = 0
#         for z in range(0, len(mat1)):
#             total = total + (mat1[x][z] * mat2[z][y])
#         row.append(total)
#     mat3.append(row)
# for x in range(0, len(mat3)):
#     for y in range(0, len(mat3[0])):
#         print (mat3[x][y], end=' ')
#     print ()

matrix = []

print("Masukkan elemen-elemen matriks 3x3 (bilangan bulat):")
for i in range(3):
    baris = []
    for j in range(3):
        elemen = int(input(f"Elemen [{i+1},{j+1}]: "))
        baris.append(elemen)
    matrix.append(baris)

print("Matriks yang dimasukkan:")
for baris in matrix:
    for elemen in baris:
        print(elemen, end=" ")
    print()

ganjil = 0
genap = 0

for baris in matrix:
    for elemen in baris:
        if elemen % 2 == 0:
            genap += 1
        else:
            ganjil += 1

print("Banyaknya Elemen Matriks Berupa Bilangan Ganjil =", ganjil)
print("Banyaknya Elemen Matriks Berupa Bilangan Genap =", genap)