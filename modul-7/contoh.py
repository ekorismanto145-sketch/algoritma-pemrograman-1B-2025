# nilai = {"Andi": 85, "Budi": 90, "Citra": 78, "Dewi": 92, "Eka": 88}

# tertinggi = max(nilai, key=nilai.get)
# rata = sum(nilai.values()) / len(nilai)

# print("Tertinggi:", tertinggi, "-", nilai[tertinggi])
# print("Rata-rata:", rata)

# make a dictionary
# data = {
#     # "key" : "value"
#     "nama" : "aris", "umur" : 20
# }

# print(data["umur"])
# print(data.get("alamat", "Data Belum ada"))

# # .get()

# data["nama"] = "eko"
# data["umur"] += 1
# print(data)

# siswa = {
#     "s1" : {"nama" : "koris", "nilai" : 88},
#     "s2" : {"nama" : "anto", "nilai" : 92}
# }

# print(siswa["s1"]["nilai"])

# contoh list di dalam dictionary
# nilai  = {
#     "aris": [88, 94, 98],
#     "wildan" : [89, 90, 96]
# }

# print(nilai["wildan"][1])

# produk = [
#     {"nama":"mouse", "harga": "15000"},
#     {"nama":"keyboard", "harga": "75000"}

# ]

# print(produk[1]["harga"])

# # set
# angka = {1,2,3,4,4,4,5}
# angka.add(7)
# print(angka)

# # buat set
# buah = {"apel", "mangga"}
# buah.remove("apel")
# buah.add("jeruk")
# print(buah)


# Contoh cara membuat Dictionary pada python

# dict = {'nama':'zara', 'age': 7, 'class': 'first'}
# print("dict['name']: ",dict['name'])
# print("dict['age']: ",dict['age'])

# # Update dictionary di python

# dict = {'nama':'zara', 'age': 7, 'class': 'first'}
# dict['age'] = 8 #mengubah entry yang sudah ada
# dict['school'] = 'DPS school' #menambah entry baru

# print("dict['age']: ",dict['age'])
# print("dict['school']: ",dict['school'])


# # Contoh cara menghapus pada Dictionary python

# dict = {'nama':'zara', 'age': 7, 'class': 'first'}

# del dict ['name'] #hapus entry dengan key 'name'
# dict.clear() #hapus semua entry di dict
# del dict # hapus dictionary yang sudah ada

# print("dict['age] :", dict['age'])
# print("dict['school']: ",dict['school'])



# ALPRO
# Membuat Dictionary
# pak_tani = {
#     "nama": "Petani Kode",
#     "umur": 22,
#     "hobi": ["coding", "membaca", "cocok tanam"],
#     "menikah": False,
#     "sosmed": {
#         "facebook": "petanikode",
#         "twitter": "@petanikode"
#     } 
# }

# # Mengakses isi dictionary
# print("Nama saya adalah %s" % pak_tani["nama"])
# print("Twitter: %s" % pak_tani["sosmed"]["twitter"])

# Membuat dictionary
# web = {
#     "name": "petanikode",
#     "url": "https://www.petanikode.com",
#     "rank": "5"
# }

# # Mencetak isi dictionary dengan perulangan
# for key in web:
#     print(web[key])

# web = {
#     "name": "petanikode",
#     "url": "https://www.petanikode.com",
#     "rank": "5"
# }

# for key, val in web.items():
#     print("%s : %s" % (key, val))


# # membuat dictioanary
# skill = {
#     "utama": "Python",
#     "lainnya": ["PHP","Java", "HTML"]
# }

# # Mencetak isi skill utama
# print(skill["utama"])

# # mengubah isi skill utama
# skill["utama"] = "Rust"

# # Mencetak isi skill utama
# print(skill["utama"])


# # membuat dictionary user
# user = {
#     "name": "petanikode"
# }

# # menambahkan password
# user.update({"password": "petani123"})

# print(user)

# # update name
# user.update({"name": "peternaklinux"})

# print(user)


# membuat dictonary
books = {
    "python": "Menguasai Python dalam 2028 jam",
    "java": "Tutorial Belajar untuk Pemula",
    "php": "Membuat aplikasi web dengan PHP"
}

# mencetak jumlah data yang ada di dalam dictionary
print("total buku: %d" % len(books))
