angka = []

def tambah():
    n = input("Masukkan angka: ")
    for i in n:
        angka.append(int(i))

def tampilkan():
    print("Daftar angka:", angka)

def ubah():
    if not angka:
        print("ga bisa, kan belum masuk angka!\n")
        return
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin diubah: "))
    if 0 <= idx < len(angka):
        angka[idx] = int(input("Masukkan angka baru: "))
    else:
        print("Indeks tidak valid.")

def hapus():
    if not angka:
        print("ga bisa, kan belum masuk angka!\n")
        return
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin dihapus: "))
    if 0 <= idx < len(angka):
        del angka[idx]
    else:
        print("Indeks tidak valid.")

def cek_bisa_dibagi():
    if not angka:
        print("ga bisa, kan belum masuk angka!\n")
        return
    total = 0
    for i in angka:
        total += i
    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi sama)")
        return
    setengah = total // 2
    sum_kiri = 0
    for i in angka:
        sum_kiri += i