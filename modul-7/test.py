# buat dictionary yang didalamnya ada 2 dict, setiap dict memiliki value list

data = {
    "barang1": {
        "nama": "Pensil",
        "stok": [10, 12, 15]
    },
    "barang2": {
        "nama": "Buku",
        "stok": [5, 7, 9]
    }
}

print(data["barang1"]["nama"])
print(data["barang1"]["stok"][1])