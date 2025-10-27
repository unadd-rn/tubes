#Guys aku pusing ini anggep aja kita ambil tol Cipali


#================================= KAMUS ===================================================
#---------------------------------Setting---------------------------------------------------
#tarif_cipali = int (ini tuh tarif dihtung dari gerbang cipali, cuma nanti kita masuk sesuai input pengguna)
#gerbang = string

#------------------------------dalam sistem---------------------------------
# Masukk
#lokasi_masuk = int(input) = nanti kita kasih pilihan terus mereka input angka
#gerbang_masuk = gerbang[lokasi_masuk] = string
#jarak_masuk = jarak_cipali[lokasi_masuk]
#tarif_masuk = tarif_cipali[lokasi_masuk] = int

# Keluarr
#lokasi_keluar = konsepnya sama kayak lokasi masuk
#gerbang_keluar = gerbang[lokasi_keluar] = string
#jarak_keluar = jarak_cipali[keluar]
#tarif_keluar = tarif_cipali[lokasi_keluar]

# Pembayaran
# Ini jadiin def aja biar bisa aku call di akhir pls <3
# semuanya sih dijadiin def kalau bisa, aku bingung kalau ga def dipanggilnya gimana
# nanti fungsi pembayaran def pembayaran() aja yak
# def pembayaran = bool aja hasilnya


import time, sys

# ==================== DATA DASAR ==========================================
gerbang = ["Cikopo", "Kalijati", "Subang", "Cikedung", "Kertajati", "Sumberjaya", "Palimanan"]

tarif_cipali = [0, 30500, 75500, 90500, 97000, 115000, 132000]

golonganKendaraan = [
    "Mobil Penumpang Umum",
    "Truk Kecil Dua Gandar",
    "Truk Tiga Gandar",
    "Truk Besar Empat Gandar",
    "Truk Lima Gandar atau Lebih"
]

# ==================== SISTEM GERBANG MASUK =================================

# Input saldo
saldo = int(input("Masukkan saldo awal kartu e-toll Anda (Rp): "))
kartu = True  # misal kartunya kita anggep aktif

# ini daftar gerbang
print("Daftar Gerbang Tol:")
for i in range(len(gerbang)):
    print(i + 1, ".", gerbang[i])

# ini masukkin lokasi masuk
lokasi_masuk = int(input("Masukkan nomor gerbang masuk: "))
if lokasi_masuk < 1 or lokasi_masuk > len(gerbang) - 1:
    print("Pilihan tidak valid!")

gerbang_masuk = gerbang[lokasi_masuk - 1]
jarak_masuk = jarak_cipali[lokasi - 1]
tarif_masuk = tarif_cipali[lokasi - 1]

# ini milih golongan kendaraan
print("Daftar Golongan Kendaraan:")
for i in range(len(golonganKendaraan) - 1):
    print(i + 1, ".", golonganKendaraan[i])

golongan = int(input("Masukkan golongan kendaraan (1-5): "))
if golongan < 1 or golongan > 5:
    print("Pilihan tidak valid!")

# bingungg ini anggep kedeteksi kartu e-toll
deteksi = input("Tempelkan kartu e-toll (ketik 'ya' jika terdeteksi): ")

if deteksi.lower() == "ya":
    print("✅ Kartu terdeteksi")
    print("Lokasi masuk:", lokasiMasuk)
    print("Golongan kendaraan:", golonganKendaraan[golongan - 1])
    print(f"Saldo Anda saat ini: Rp{saldo}")

    print("🚧 Palang sedang dibuka", end="")
    print_slow("......")
    
    print_slow("🚗💨💨💨💨💨💨💨💨💨💨")

    print("✅ Palang tertutup kembali. Selamat berkendara!\n")

else:
    print("❌ Kartu tidak terbaca. Akses ditolak.")



# ==================== SISTEM GERBANG KELUAR =================================
def gerbang_keluar():
    keluar = input("Masukkan gerbang keluar:")
    waktu_keluar = input("Masukkan waktu keluar: ")

    #ini tarif_masuk definisiin di bagian Aufa
    #tarif_keluar definisiin di bagian livy
    tarif = tarif_keluar - tarif_masuk
    if pembayaran(tarif):
        print(" ______________________"); time.sleep(0.2)
        print("|                       |"); time.sleep(0.2)
        print("|                       |"); time.sleep(0.2)
        print("|     Selamat Jalan!    |"); time.sleep(0.2)
        print("|                       |"); time.sleep(0.2)
        print("|                       |"); time.sleep(0.2)
        print("|_______________________|"); time.sleep(0.2)

        print_slow("🚗💨💨💨💨💨💨💨💨💨💨")



# ==================== PEMBAYARAN =================================
def pembayaran():
    #cek apakah kartu terdefinisi
    if kartu is None:
        print("kartu tidak terbaca")
        return False
    
    #cek apakah saldo cukup
    if saldo>=tarif :
        saldo-=tarif
        print("pembayaran berhasil!")
        print("sisa saldo: Rp" +str(saldo))
        return True
    else:
        print("saldo tidak cukup")
        return False












