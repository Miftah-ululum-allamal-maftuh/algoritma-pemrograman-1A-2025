lama_parkir = int(input("Berapa lama kamu parkir(jam): "))
vip = input("Apakah memmber VIP? (ya/tidak): ")

tarif_awal = 5000
tarif_per_jam = 3000
tarif_harian = 20000

if vip == "ya":
    total = 0
else:
    jumlah_hari = lama_parkir // 24 5

sisa_jam = lama_parkir % 24
total_hari = jumlah_hari * 20000

if sisa_jam == 0:
    sisa_jam = 0
elif sisa_jam <= 2:
    sisa_jam = tarif_awal
else:
    sisa_jam = tarif_awal + (sisa_jam - 2) * 3000
if sisa_jam >= tarif_harian:
    sisa_jam = tarif_harian * sisa_jam
total = total_hari + sisa_jam

print("\nTotal biaya parkir: Rp", f"{total:,}")