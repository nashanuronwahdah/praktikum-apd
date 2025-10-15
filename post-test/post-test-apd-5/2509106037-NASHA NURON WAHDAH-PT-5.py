import os

# Akun Admin
admin = 'ADMIN'
pw1 = '4321'

# Akun User 
user = 'Nuron'
pw2 = '1234'

# Nested List sebagai List Penumpang Yang terdaftar 
penumpang = [
    [1, ""],
    [2, "Bakil"],
    [3, ""],
    [4, ""],
    [5, "Nuron"],
    [6, "Riyad"]
]

# Boolean untuk membantu loop 
keluar = False

# Intro 
print('SELAMAT DATANG DI PENERBANGAN FUFUFAFA-AIR')
print('SILAHKAN LOGIN SESUAI AKUN ANDA')
input_nama = input('Silahkan Masukkan Username anda: ')
input_pw = input('Silahkan Masukkan Password anda: ')

# Akun Admin 
if input_nama == 'ADMIN' and input_pw == '4321':
    os.system('cls || clear')
    
    print('ANDA BERHASIL LOGIN SEBAGAI ADMIN!')
    while not keluar:
        print('SILAHKAN PILIH MENU YANG INGIN ANDA GUNAKAN: ')
        print('1. CEK LIST PENUMPANG YANG SUDAH TERDAFTAR')
        print('2. TAMBAH ATAU HAPUS LIST PENUMPANG')
        print('3. KELUAR DARI PROGRAM')
        input_admin = input('Masukkan Input(Hanya Angka): ')

        if input_admin == '1':
            os.system('cls || clear')
            print('Berikut adalah list penumpang sesuai tempat duduk')
            print('Jika kosong, berarti kursi belum terjual')
            print( penumpang )
            input_admin2 = input('KETIK 1 untuk keluar: ')
            if input_admin2 == '1':
                continue
            else:
                print('INPUT TIDAK VALID!')
                continue

        elif input_admin == '2':
            os.system('cls || clear')
            print('Berikut adalah list penumpang sesuai tempat duduk')
            print( penumpang )
            print('Silahkan Pilih Menu Di bawah:')
            print('1. Tambah Penumpang')
            print('2. Hapus Penumpang')
            print('3. Kembali ke Program Sebelumnya')
            input_admin2 = input('Silahkan Masukkan Input (Hanya Angka): ')
           
            if input_admin2 == '1':
                os.system('cls || clear')
                print (penumpang)
                nomor_kursi = int(input('Silahkan pilih nomor kursi: '))
                nama_penumpang = input('Silahkan isi nama penumpang: ')
                if 1 <= nomor_kursi <= len(penumpang):
                    
                    if penumpang[nomor_kursi - 1][1] == "":
                       penumpang[nomor_kursi - 1][1] = nama_penumpang
                       print(f'Penumpang {nama_penumpang} berhasil ditambahkan di kursi {nomor_kursi}!')
                       continue
                    else:
                        os.system('cls || clear')
                        print('Kursi tersebut sudah terisi!')
                        continue
                else:
                     os.system('cls || clear')
                     print('Nomor kursi tidak valid!')
                     continue

            elif input_admin2 == '2':
                 os.system('cls || clear')
                 print (penumpang)
                 nomor_kursi = int(input('Masukkan Nomor Kursi yang ingin dihapus: '))

                 if 1 <= nomor_kursi <= len(penumpang):
                   if penumpang[nomor_kursi - 1][1] != "":
                      os.system('cls || clear')
                      nama = penumpang[nomor_kursi - 1][1]
                      penumpang[nomor_kursi - 1][1] = ""
                      print(f'Data penumpang {nama} di kursi {nomor_kursi} berhasil dihapus!')
                      continue
                   else:
                        os.system('cls || clear')
                        print('Kursi tersebut memang sudah kosong!')
                        continue
                 else:
                      os.system('cls || clear')
                      print('Nomor kursi tidak valid!')
                      continue
           
        elif input_admin == '3':
            os.system('cls || clear')
            print('Terima kasih telah berkunjung!')
            keluar = True

        else:
            os.system('cls || clear')
            print('Input tidak valid!')
            continue

# Akun User 
elif input_nama == 'Nuron' and input_pw == '1234':
    os.system('cls || clear')
    
    print('ANDA BERHASIL LOGIN SEBAGAI USER!')
    while not keluar:
        print('SILAHKAN PILIH MENU YANG INGIN ANDA GUNAKAN: ')
        print('1. MENGECEK TIKET YANG TERSEDIA')
        print('2. MEMBELI TIKET PESAWAT')
        print('3. KELUAR DARI PROGRAM')
        input_user = input('Masukkan Input(Hanya Angka): ')

        if input_user == '1':
            os.system('cls || clear')
            print('TIKET YANG TERSEDIA:')
            print('1. SAMARINDA TO DIDDY ISLAND [BESOK 17.30]')
            print('Penumpang yang sudah terdaftar: ')
            print(penumpang)
            input_user2 = input('KETIK 1 untuk keluar: ')
            if input_user2 == '1':
                os.system('cls || clear')
                continue
            else:
                os.system('cls || clear')
                print('Input tidak valid!')
                continue

        elif input_user == '2':
            os.system('cls || clear')
            print(penumpang)
            for kursi in penumpang:
                print(f'Kursi {kursi[0]}: {"KOSONG" if kursi[1] == "" else kursi[1]}')
            nomor_kursi = int(input('Pilih nomor kursi yang ingin anda pilih: '))
            nama_penumpang = input('Masukkan Nama Penumpang: ')

            if 1 <= nomor_kursi <= len(penumpang):
                if penumpang[nomor_kursi - 1][1] == "":
                    penumpang[nomor_kursi - 1][1] = nama_penumpang
                    os.system('cls || clear')
                    print('Tiket Berhasil Dipesan!')
                    continue
                else:
                    os.system('cls || clear')
                    print('Maaf, kursi tersebut sudah terisi!')
                    continue
            else:
                os.system('cls || clear')
                print('Nomor kursi tidak valid! Silakan pilih kursi yang tersedia.')
                continue

        elif input_user == '3':
            os.system('cls || clear')
            print('Terima kasih telah berkunjung!')
            keluar = True

        else:
            os.system('cls || clear')
            print('Input tidak valid!')
            continue

else:
    os.system('cls || clear')
    print('--SESI PROGRAM TELAH BERHENTI--')

            


            

