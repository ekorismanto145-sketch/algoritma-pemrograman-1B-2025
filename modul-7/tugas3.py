kupon = {
    "ARIS": 10,
    "EKO": 20,
    "KORIS": 30
}

keranjang = []


def tambah_barang():
    nama = input("Nama barang: ")
    
    harga_input = input("Harga barang: ")
    if not harga_input.isdigit():
        print("Harga harus berupa angka.")
        return

    harga = float(harga_input)

    keranjang.append([nama, harga])
    print(f"Barang '{nama}' dengan harga Rp{harga} berhasil ditambahkan.")


def tampilkan_barang():
    if not keranjang:
        print("Belum ada barang di keranjang.")
    else:
        print("=== BARANG DALAM KERANJANG ===")
        total = 0
        for i, item in enumerate(keranjang, start=1):
            print(f"{i}. {item[0]} - Rp{item[1]}")
            total += item[1]
        print(f"Total Belanja Saat Ini: Rp{total}")


def proses_transaksi():

    if not keranjang:
        print("Keranjang kosong. Tambah barang dulu.")
        return

    total = sum(item[1] for item in keranjang)
    print(f"Total belanja: Rp{total}")

    kode = input("Masukkan kode kupon (jika ada): ").upper()

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        total_bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Potongan: Rp{potongan}")
        print(f"Total bayar: Rp{total_bayar}")

        del kupon[kode]
        print("Kupon telah digunakan.")
    else:
        print("Kupon tidak valid atau tidak ada.")
        print(f"Total bayar tanpa diskon: Rp{total}")


def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("=== KUAPON TERSEDIA ===")
        for kode, diskon in kupon.items():
            print(f"{kode} -> {diskon}%")


while True:
    print("=== SISTEM BELANJA + KUPON ===")
    print("1. Tambah Barang Belanja")
    print("2. Tampilkan Barang & Total Belanja")
    print("3. Tampilkan Kupon")
    print("4. Proses Pembayaran")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        tampilkan_kupon()
    elif pilihan == "4":
        proses_transaksi()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
