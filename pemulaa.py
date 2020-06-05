import os, sys, time, string, random
#________________________________________________
# WARNA
normal = ("\033[1;0m")
merah = ("\033[1;31m")
hijau = ("\033[1;32m")
kuning = ("\033[1;33m")
biru = ("\033[1;34m")
ungu = ("\033[1;35m")
cyan = ("\033[0;36m")
#________________________________________________
x = ('mutez')
y = ('baik')
os.system ('clear')
os.system (' figlet Welcome | lolcat')

#________________________________________________
print (cyan)

print "_____________________________________________ "
print "		  Login!!"

print (kuning)
print 
print "Tekan (CTRL z) Untuk Berhenti"

name = raw_input ('Username : ')
passw = raw_input ('Password : ')

print (cyan)

print "_____________________________________________ "

#________________________________________________

if (name == x and passw == y) :
	print (biru)
	print "Loading..."
	time.sleep(5)
	print (hijau)
	print "Login Sucsess"
	time.sleep(1)
	os.system ('clear')
	
else :
	print (biru)
	print "Loading..."
	time.sleep(5)
	print (merah)
	print "Login Failed"
	time.sleep(1)
	print (kuning)
	print "Masukkan Yang Benar Woi!!"
	time.sleep(3)
	os.system('python2 mutez.py')

	print (normal)
#____________________________________________________

os.system ('figlet MuTe-Z | lolcat')

print (merah)

print "=================================================="

print (ungu)

print "Yang Punya : Mr.MuTe-Z"
print "Instagram  : mute__z"
print "YouTube    : (Lagi Proses Pembuatan)"

print (merah)

print "=================================================="
print

print (cyan)
print "[.] Menu Pilihan [.]"
print
print "[1] Melihat System Android "
print "[2] Mengecek Ip Kamu "
print "[3] Menampilkan Tombol Kiri Dan Kanan"
print "[4] Cara Memperlancar Koneksi Jaringan "
print "[0] Exit"
print

#_______________________________________________
print (cyan)
pilih = raw_input('[?] Pilih : ')
#_______________________________________________

if pilih == "0":
	print (merah)
	print
	print "Exit!"
	time.sleep(2)
	os.system('clear')
	exit()
	print (normal)
#_______________________________________________
if pilih == "1":
	os.system ('clear')

	print (hijau)

	print "Menginstal..."
	time.sleep(2)
	print (normal)
	os.system ('pkg install neofetch')

	print (hijau)

	print "Sucsess"
	time.sleep(2)
	print (biru)
	print "Loading..."
	time.sleep(1)
	os.system('clear')
	print
	print (cyan)
	print "Memproses [][][]"
	os.system('neofetch')
	print
	print (hijau)
	print ("Terima Kasih")
	time.sleep(99999)
	print
	print "Tekan (CTRL z) Untuk Berhenti"
	print (normal)
#_______________________________________________

if pilih == "2":
	os.system ('clear')
	print (cyan)
	print "Sedang Memproses..."
	time.sleep(3)
	print (hijau)
	print ('Sucsess')
	time.sleep(3)
	print (kuning)
	print "Note: Tonton Video Channel MuTeZ"
	print "Untuk Mengetahui Posisi Ip Kalian"
	time.sleep(7)
	print (normal)
	os.system ('clear')
	os.system ('ifconfig')
	print (hijau)
	print
	print "Tekan (CTRL z) Untuk Berhenti"
	time.sleep(999999)
	print (normal)

#_______________________________________________

if pilih == "3":
	os.system('clear')
	print (hijau)
	print "Menginstal..."
	time.sleep(3)
	print (normal)
	os.system ('pkg install git')
	print (kuning)
	print
	print "Selesai"
	time.sleep(2)
	os.system ('clear')
	print (hijau)
	print "Memproses..."
	time.sleep(3)
	os.system('git clone https://github.com/BangDanz/home')
	time.sleep(2)
	print (hijau)
	print "Sucsess"
	time.sleep(2)
	print (kuning)
	print 
	print "Selamat Menikmati"
	print (3)
	print
	print (ungu)
	print "Login Ulang..."
	time.sleep(8)
	os.system('python2 mutez.py')
	print (normal)
#_______________________________________________
if pilih == "4":
	print (kuning)
	os.system ('clear')
	print
	print
	print
	print "Kamu Harus Copy Ip Kamu Dahulu"
	print
	time.sleep(2)
	print "Jika Sudah "
	print
	time.sleep(2)
	print "Untuk Mempermudah Kamu Tinggal Copy Saja Yang Dibawah Ini"
	print
	time.sleep(2)
	print
	print "		ping -s 9000	 "
	print
	print
	print
	time.sleep(8)
	print "Kamu Harus Paste Ip Kamu Lalu Tekan Enter"
	time.sleep(5)
	print
	print (hijau) 
	print "Selamat Mencoba Guys"
	print
	print
	print