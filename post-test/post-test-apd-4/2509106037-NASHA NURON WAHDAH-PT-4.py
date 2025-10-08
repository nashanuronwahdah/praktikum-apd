import os

# Akun User 
username = 'Nuron'
pw = '037'

# Boolean dan variabel untuk membantu akses dan batas login
percobaan_maks = 5
coba = False

# Perulangan, batas maksimal user salah input login adalah 5 kali
percobaan = 0
while percobaan < percobaan_maks and not coba:
    print('=========SELAMAT DATANG DI RENTAL MOBIL PAK HARI=========')
    print('---SILAHKAN LOGIN SESUAI USERNAME DAN PASSWORD ANDA---')
    
    input_username = input('Silahkan masukkan username akun anda: ')
    input_pw = input('Silahkan masukkan password akun anda: ')

    if input_username == username and input_pw == pw:
        os.system('cls')
        print('Horee, Login anda sukses!')
        coba = True
    elif percobaan < percobaan_maks - 1:
        os.system('cls')
        percobaan += 1
        sisa_percobaan = percobaan_maks - percobaan
        print (f'Username atau Password anda salah! Sisa kesempatan login adalah {sisa_percobaan} kali')
    else:
        os.system('cls')
        print('Maaf kesempatan login sudah habis!')
        coba = False
        break

# Nah disini masuk ke biodata user untuk ditentukan apakah User bisa merental mobil  atau tidak 
if coba == True:     
    # User Menginput Data 
    percabangan = False
    while not percabangan:
        print('Karena Kebutuhan Biodata, silahkan isi data di bawah sesuai dengan data anda: ')
        usia = int(input('Silahkan masukkan usia anda (hanya angka): '))
        SIM = int(input('Apakah anda memiliki SIM A? (Ketik 1 untuk ya, dan 2 untuk tidak): '))
        deposit = int(input('Silahkan masukkan deposit anda (hanya angka): '))
        pengalaman = int(input('Silahkan masukkan, berapa tahun pengalaman anda dalam mengemudi mobil (hanya angka): '))

        # Percabangan 
        if usia < 21:
            os.system('cls')
            print('Maaf, usia anda tidak mencukupi, program akan kembali ke input biodata')
            percabangan = False

        elif SIM != 1 and SIM != 2:
            os.system('cls')
            print('Input Perintah SIM Anda Salah! Program akan kembali ke input biodata')
            percabangan = False

        elif SIM == 2:
            os.system('cls')
            print('Maaf, anda harus memiliki SIM A! Program akan kembali ke input biodata')
            percabangan = False
        
        elif deposit < 500000:
            os.system('cls')
            print('Maaf, Deposit anda kurang. Deposit minimal adalah Rp500.000')
            print('Program akan kembali ke biodata')
            percabangan = False

        elif pengalaman < 4:
            os.system('cls')
            print('Karena pengalamanmu kurang dari 4 tahun, maka kamu hanya bisa menyewa mobil standar')
            standar = int(input('Ketik 1 untuk setuju, ketik 2 untuk tidak: '))
            if standar == 1:
                print('Oke terima kasih! Mobil akan meluncur secepatnya!!!')
                percabangan = True
            elif standar == 2:
                print('Oke, mungkin lain kali ya!')
                percabangan = True
            else:
                print('Input Anda Salah! Program akan kembali ke biodata')
                percabangan = False

        elif pengalaman >= 4:
            os.system('cls')
            print('Anda bisa memilih semua jenis mobil!')
            premium = int(input('Ketik 1 untuk mobil standar, ketik 2 untuk mobil premium: '))

            if premium == 1 or premium == 2:
                print('Oke terima kasih! Mobil akan meluncur secepatnya!!!')
                percabangan = True
            else:
                print('Input Anda Salah! Program akan kembali ke biodata')
                percabangan = False

        else:
            os.system('cls')
            print('Input Anda Salah!')
else:
    print('Program akan berhenti ya!')




