#Guys aku pusing ini anggep aja kita ambil tol Cipali


#==================== KAMUS ===================================================
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
jarak_cipali = [72, 98, 109, 137, 158, 174, 188]

golonganKendaraan = [
    "Mobil Penumpang Umum",
    "Truk Kecil Dua Gandar",
    "Truk Tiga Gandar",
    "Truk Besar Empat Gandar",
    "Truk Lima Gandar atau Lebih"
]

# ==================== SISTEM GERBANG MASUK =================================
print("=== SISTEM GERBANG MASUK TOL CIPALI ===")

# Input saldo
saldo = int(input("Masukkan saldo awal kartu e-toll Anda (Rp): "))
kartu = True  # simulasi kartu aktif

# Tampilkan daftar gerbang
print("Daftar Gerbang Tol:")
for i in range(len(gerbang)):
    print(i + 1, ".", gerbang[i])

# Input lokasi masuk
lokasi_masuk = int(input("Masukkan nomor gerbang masuk: "))
if lokasi_masuk < 1 or lokasi_masuk > len(gerbang):
    print("Pilihan tidak valid!")

gerbang_masuk = gerbang[lokasi_masuk - 1]
jarak_masuk = jarak_cipali[lokasi - 1]
tarif_masuk = tarif_cipali[lokasi - 1]

# Pilih golongan kendaraan
print("Daftar Golongan Kendaraan:")
for i in range(len(golonganKendaraan)):
    print(i + 1, ".", golonganKendaraan[i])

golongan = int(input("Masukkan golongan kendaraan (1-5): "))
if golongan < 1 or golongan > 5:
    print("Pilihan tidak valid!")

# Simulasi deteksi kartu e-toll
deteksi = input("Tempelkan kartu e-toll (ketik 'ya' jika terdeteksi): ")

if deteksi.lower() == "ya":
    nomorKartu = input("Masukkan nomor kartu e-toll: ")
    print("✅ Kartu terdeteksi")
    print("Nomor kartu:", nomorKartu)
    print("Lokasi masuk:", lokasiMasuk)
    print("Golongan kendaraan:", golonganKendaraan[golongan - 1])
    print(f"Saldo Anda saat ini: Rp{saldo}")

    # Animasi masuk tol
    print("🚧 Palang sedang dibuka", end="")
    for i in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print_slow("🚗💨💨💨💨💨💨💨💨💨💨")

    print("✅ Palang tertutup kembali. Selamat berkendara!\n")

else:
    print("❌ Kartu tidak terbaca. Akses ditolak.")

def gerbang_keluar():
    keluar = input("Masukkan gerbang keluar:")
    waktu_keluar = input("Masukkan waktu keluar: ")

    #jarak_masuk definisiin di bagian aufa
    #jarak_keluar definisiin di bagian livy

    jarak = jarak_keluar - jarak_masuk

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

        def print_slow(str):
            for letter in str:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.2)

        print_slow("🚗💨💨💨💨💨💨💨💨💨💨")


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






