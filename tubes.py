# Guys aku pusing ini anggep aja kita ambil tol Cipali


# ================================= KAMUS ===================================================
# ---------------------------------Setting---------------------------------------------------
# tarif_cipali = int (ini tuh tarif dihtung dari gerbang cipali, cuma nanti kita masuk sesuai input pengguna)
# gerbang = string

# ------------------------------dalam sistem---------------------------------
# Masukk
# lokasi_masuk = int(input) = nanti kita kasih pilihan terus mereka input angka
# gerbang_masuk = gerbang[lokasi_masuk] = string
# jarak_masuk = jarak_cipali[lokasi_masuk]
# tarif_masuk = tarif_cipali[lokasi_masuk] = int

# Keluarr
# lokasi_keluar = konsepnya sama kayak lokasi masuk
# gerbang_keluar = gerbang[lokasi_keluar] = string
# jarak_keluar = jarak_cipali[keluar]
# tarif_keluar = tarif_cipali[lokasi_keluar]

# Pembayaran
# Ini jadiin def aja biar bisa aku call di akhir pls <3
# semuanya sih dijadiin def kalau bisa, aku bingung kalau ga def dipanggilnya gimana
# nanti fungsi pembayaran def pembayaran() aja yak
# def pembayaran = bool aja hasilnya

# ==================== DATA DASAR =================================
gerbang = ["Cikopo", "Kalijati", "Subang", "Cikedung",
           "Kertajati", "Sumberjaya", "Palimanan"]

tarif_cipali = [0, 30500, 75500, 90500, 97000, 115000, 132000]
pengali_golongan = [1, 1.5, 1.5, 2, 2]

golonganKendaraan = ["Mobil penumpang umum", "Truk kecil 2 gandar",
                     "Truk 3 gandar", "Truk 4 gandar", "Truk 5 gandar"]

# ==================== GERBANG MASUK =================================

saldo = int(input("Masukkan saldo awal kartu e-toll Anda (Rp): "))
print()
kartu = True  # misal kartu aktif

lokasisesuai = False
while lokasisesuai == False:
    print("Daftar Gerbang Tol:")
    for i in range(len(gerbang) - 1):
        print(f"{i + 1}.", gerbang[i])
    lokasi_masuk = int(input("Masukkan nomor gerbang masuk: "))

    if lokasi_masuk >= 1 and lokasi_masuk < len(gerbang):
        gerbang_masuk = gerbang[lokasi_masuk - 1]
        tarif_masuk = tarif_cipali[lokasi_masuk - 1]
        lokasisesuai = True
    else:
        print("❌Pilihan tidak valid! Silakan ulangi.")
    print()

golongansesuai = False
while golongansesuai == False:
    print("Daftar Golongan Kendaraan:")
    for i in range(len(golonganKendaraan)):
        print(f"{i + 1}. Golongan {i+1}:", golonganKendaraan[i])
    golongan = int(input("Masukkan golongan (1-5): "))
    if golongan >= 1 and golongan <= 5:
        golongansesuai = True
    else:
        print("❌Pilihan tidak valid! Silakan ulangi.")
    print()

kartuterdeteksi = False
while kartuterdeteksi == False:
    deteksi = input("Tempelkan kartu e-toll (ketik 'ya' jika terdeteksi): ")
    if deteksi.lower() == "ya":
        kartuterdeteksi = True
        print()
        print("✅ Kartu terdeteksi")
        print()
        print("========================================")
        print("Lokasi masuk       :", gerbang_masuk)
        print("Golongan kendaraan :", golonganKendaraan[golongan - 1])
        print("Saldo Anda saat ini: Rp", saldo)
        print("========================================")
    else:
        print("❌ Kartu tidak terbaca. Coba lagi.")
    print()

print("🚧 Palang sedang dibuka...")
print("✅ Palang tertutup kembali. Selamat berkendara!")
print()

# ==================== DALAM TOL =================================
tarif_keluar = 0
posisi = lokasi_masuk - 1

while True:
    if posisi == 6:
        print(f"Anda ada di gerbang terakhir, tol {gerbang[posisi]}")
        break
    elif posisi+1 <= 6:
        print(f"Anda sedang berada di tol {gerbang[posisi]}")
        print(f"1. Lanjut ke tol {gerbang[posisi+1]}")
        print(f"2. Keluar tol")

    pilihan = input("Pilihan Anda (1/2): ")
    print("========================================")
    if pilihan == "1":
        tarif_keluar = tarif_cipali[posisi + 1]
        posisi += 1
    elif pilihan == "2":
        print(f"Anda keluar dari tol {gerbang[posisi]}")
        break
    else:
        print("Pilihan Anda tidak valid, silakan coba lagi.")

# ==================== GERBANG KELUAR =================================

pengali = pengali_golongan[golongan - 1]
gerbang_keluar = gerbang[posisi]

tarif = (tarif_keluar - tarif_masuk)*pengali

print("🚗 Anda mendekati gerbang keluar...")

while True:
    deteksi = input("Tempelkan kartu e-toll (ketik 'ya' jika terdeteksi): ")
    if deteksi.lower() == "ya":
        break
    else:
        print("❌ Kartu tidak terbaca di gerbang keluar. Silakan coba lagi atau hubungi petugas.")

print("✅ Kartu terdeteksi")

print()

print("Mengecek data perjalanan...", end="")
print("......")
print("Data berhasil dibaca")

print()

print("========================================")
print(f"Gerbang Masuk : {gerbang_masuk}")
print(f"Gerbang Keluar: {gerbang_keluar}")
print(f"Golongan      : {golonganKendaraan[golongan - 1]}")
print(f"Total tarif   : Rp{tarif:}")
print("========================================")

print()

print("Melanjutkan ke proses pembayaran")

# ==================== PEMBAYARAN =================================
if not kartu:
    print("❌ Kartu tidak terbaca.")
else:
    if saldo >= tarif:
        saldo -= tarif
        print("✅ Pembayaran berhasil!")
        print("Sisa saldo: Rp", saldo)

        print()
        print(" ______________________")
        print("|                       |")
        print("|                       |")
        print("|     Selamat Jalan!    |")
        print("|                       |")
        print("|                       |")
        print("|_______________________|")
        # print_slow("🚗💨💨💨💨💨💨💨💨💨💨")

    else:
        print("❌ Saldo tidak cukup.")


