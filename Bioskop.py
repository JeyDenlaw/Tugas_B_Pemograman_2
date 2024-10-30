harga_tiket = {
    "reguler": 50000,
    "vip": 100000
}

hitung_harga = lambda tipe, member: harga_tiket.get(tipe.lower(), 0) * (0.8 if member else 1)

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ")
is_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower() == "ya"

total_harga = hitung_harga(tipe_tiket, is_member)
if total_harga == 0:
    print("Tipe tiket tidak valid.")
else:
    print(f"Total harga yang harus dibayar: Rp{total_harga}")