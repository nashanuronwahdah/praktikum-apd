# Program Biodata Penumpang Pesawat Stecu Air 

#Intro Program
print('===SELAMAT DATANG DI PROGRAM BIODATA PENUMPANG PESAWAT STECU AIR===')
print('--Silahkan Isi Biodata Berikut-- ')

# User Menginput Biodata
nama = str(input('Silahkan masukkan nama penumpang: '))
usia = int(input('Silahkan masukkan usia penumpang (Hanya Angka): '))
tiket =int(input('Silahkan masukkan nomor tiket: '))
berat = float(input('Silahkan masukkan berat bagasi penumpang (dalam kg): '))

# Print Biodata Yang Telah User Input 
print('==BIODATA PENUMPANG PESAWAT STECU AIR==')
print('Nama: ' + nama)
print('Usia: ' + str(usia) + ' tahun')
print('Nomor Tiket: ' + str(tiket) )
print('Berat Bagasi: ' + str(berat) + ' kg')
print('Verifikasi Tiket Asli atau Bukan: ' + str(bool(usia)))
