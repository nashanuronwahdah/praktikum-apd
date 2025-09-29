# Intro 
print('=========SELAMAT DATANG DI RENTAL MOBIL PAK HARI=========')
print('---SILAHKAN ISI BIODATA TERLEBIH DAHULU---')

# User Menginput Data 
nama = str(input('Silahkan masukkan nama anda: '))
usia = int(input('Silahkan masukkan usia anda (hanya angka): '))
SIM = int(input('Apakah anda memiliki SIM A? (Ketik 1 untuk ya, dan 2 untuk tidak): '))
deposit = int(input('Silahkan masukkan deposit anda (hanya angka): '))
pengalaman = int(input('Silahkan masukkan, berapa tahun pengalaman anda dalam mengemudi mobil (hanya angka): '))

# Percabangan 
if usia < 21:
    print('Maaf, usia anda tidak mencukupi')

elif SIM != 1 and SIM != 2:
    print('Input Perintah SIM Anda Salah!')

elif SIM == 2:
    print('Maaf, anda harus memiliki SIM A')
  
elif deposit < 500000:
    print('Maaf, Deposit anda kurang. Deposit minimal adalah Rp500.000')

elif pengalaman < 4:
    print('Karena pengalamanmu kurang dari 4 tahun, maka kamu hanya bisa menyewa mobil standar')
    standar = int(input('Ketik 1 untuk setuju, ketik 2 untuk tidak: '))
    if standar == 1:
        print('Oke terima kasih! Mobil akan meluncur secepatnya!!!')
    elif standar == 2:
        print('Oke, mungkin lain kali ya!')
    else:
        print('Input Anda Salah!')

elif pengalaman >= 4:
    print('Anda bisa memilih semua jenis mobil!')
    premium = int(input('Ketik 1 untuk mobil standar, ketik 2 untuk mobil premium: '))

    if premium == 1 or premium == 2:
        print('Oke terima kasih! Mobil akan meluncur secepatnya!!!')
    else:
        print('Input Anda Salah!')

else:
    print('Input Anda Salah!')





