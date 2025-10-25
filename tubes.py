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


tarif_cipali = {
    0,
    30500,
    75500,
    90500,
    97000,
    115000,
    132000
}

jarak_cipali = {
    72,
    98,
    109,
    137,
    158,
    174,
    188
}

gerbang = {
    "Cikopo", 
    "Kalijati", 
    "Subang", 
    "Cikedung", 
    "Kertajati", 
    "Sumberjaya", 
    "Palimanan"
    }


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

        import sys, time
        def print_slow(str):
            for letter in str:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.2)

        print_slow("🚗💨💨💨💨💨💨💨💨💨💨")
