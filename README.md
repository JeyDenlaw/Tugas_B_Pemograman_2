Langkah Program Kalkulator.py
1. buat fungsi yang menerima 3 parameter : angka1, angka2, dan operator
2. lalu periksa operator
   Jika Operator adalah '+' kembalikan hasil penjumlahan angka1 dan angka2
   Periksa seluruh Operator '-' dan '*'
   Jika Operator adalah '/' periksa apakah angka2 tidak sama dengan 0, jika tidak kembalikan hasil pembagian angka1 dan angka2, jika iya, kembalikan pesan error.
   Jika Operator tidak Valid, kembalikan pesan "Operator tidak Valid"

3. selanjutnya, minta pengguna untuk memasukkan angka1 dan angka2 dengan angka desimal, serta minta pengguna untuk memasukkan Operator
4. lalu, program akan memanggil fungsi kalkulator dengan input dari pengguna dan menyimpan hasilnya
5. selanjutnya, hasil dari perhitungan akan di cetak dan di tampilkan

Langkah Program Bioskop.py
1. Buat Dictionary harga_tiket untuk menyimpan harga tiket reguler dan VIP
2. Buat fungsi lambda hitung_harga yang menerima dua parameter: tipe dan member. Fungsi ini akan mengembalikan harga tiket berdasarkan tipe dan apakah pengguna memiliki kartu member (Pengguna akan mendapatkan diskon 20% jika memiliki member)
3. Minta pengguna untuk memasukkan tipe_tiket (reguler atau VIP), dan Minta pengguna memasukkan status member (ya atau tidak).
4. panggil fungsi hitung_harga dengan input dari pengguna dan simpan hasilnya di total_harga
5. Jika total_harga adalah 0, Cetak pesan "Tipe tiket tidak valid". Jika tidak, cetak total harga yang harus dibayar.
