import os

# Akun Admin 
admin = 'ADMIN' 
pw1 = '4321' 

# Akun User 
user = 'Nuron' 
pw2 = '1234'

# Dictionary sebagai List Penumpang Yang terdaftar 
penumpang = {
    1: "",
    2: "Bakil",
    3: "",
    4: "",
    5: "Nuron",
    6: "Riyad"
}

# Fungsi Tanpa Parameter 
def Input():
    return "Masukkan Input(Hanya Angka): "

def tidakvalid():
    return "TIDAK VALID!"

# Fungsi Dengan Parameter 
def login(akun):
    print(f"ANDA BERHASIL LOGIN SEBAGAI {akun}!")
    
def tampilkan_menu(akun):
    print("SILAHKAN PILIH MENU YANG INGIN ANDA GUNAKAN:")
    if akun == 'ADMIN_1':
        print('1. CEK LIST PENUMPANG YANG SUDAH TERDAFTAR')
        print('2. TAMBAH ATAU HAPUS LIST PENUMPANG')
        print('3. KELUAR DARI PROGRAM')
    elif akun == 'ADMIN_2':
        print('1. Tambah Penumpang')
        print('2. Hapus Penumpang')
        print('3. Kembali ke Program Sebelumnya')
    elif akun == 'USER':
        print('1. MENGECEK TIKET YANG TERSEDIA')
        print('2. MEMBELI TIKET PESAWAT')
        print('3. KELUAR DARI PROGRAM')
        
# Fungsi Prosedural 
def beli_tiket():
    for kursi, nama in penumpang.items():
        print(f'Kursi {kursi}: {"KOSONG" if nama == "" else nama}')
        
def list_penumpang():
    print('Berikut adalah list penumpang sesuai tempat duduk')
    
# Variabel Global
tujuan_penerbangan = "SAMARINDA TO DIDDY ISLAND"
jadwal_penerbangan = "BESOK 17.30"
maks_kursi = 6

# Boolean untuk membantu loop 
keluar = False

while True:

    # Intro 
    print('SELAMAT DATANG DI PENERBANGAN FUFUFAFA-AIR')
    print('SILAHKAN LOGIN SESUAI AKUN ANDA')
    input_nama = input('Silahkan Masukkan Username anda: ')
    input_pw = input('Silahkan Masukkan Password anda: ')

    # Akun Admin 
    if input_nama == 'ADMIN' and input_pw == '4321':
        os.system('cls || clear')
        
        login('ADMIN')
        while not keluar:
            tampilkan_menu('ADMIN_1')
            input_admin = input(Input())

            if input_admin == '1':
                os.system('cls || clear')
                list_penumpang()
                print('Jika kosong, berarti kursi belum terjual')
                print( penumpang )
                input_admin2 = input('KETIK 1 untuk keluar: ')
                if input_admin2 == '1':
                    continue
                else:
                    print(tidakvalid())
                    continue

            elif input_admin == '2':
                os.system('cls || clear')
                list_penumpang()
                print( penumpang )
                tampilkan_menu('ADMIN_2')
                input_admin2 = input(Input())
            
                if input_admin2 == '1':
                    os.system('cls || clear')
                    print (penumpang)
                    try:
                        nomor_kursi = int(input('Silahkan pilih nomor kursi: '))
                    except ValueError:
                        os.system('cls || clear')
                        print(tidakvalid())
                        continue
                    nama_penumpang = input('Silahkan isi nama penumpang: ')
                    
                    if 1 <= nomor_kursi <= maks_kursi:
                        
                        if penumpang[nomor_kursi] == "":
                            penumpang[nomor_kursi] = nama_penumpang
                            print(f'Penumpang {nama_penumpang} berhasil ditambahkan di kursi {nomor_kursi}!')
                            continue
                        else:
                            os.system('cls || clear')
                            print('Kursi tersebut sudah terisi!')
                            continue
                    else:
                        os.system('cls || clear')
                        print('Nomor kursi ' + tidakvalid())
                        continue

                elif input_admin2 == '2':
                    os.system('cls || clear')
                    print (penumpang)
                    try:
                        nomor_kursi = int(input('Masukkan Nomor Kursi yang ingin dihapus: '))
                    except ValueError:
                        os.system('cls || clear')
                        print(tidakvalid())
                        continue


                    if 1 <= nomor_kursi <= maks_kursi:
                        if penumpang[nomor_kursi] != "":
                            os.system('cls || clear')
                            nama = penumpang[nomor_kursi]
                            penumpang[nomor_kursi] = ""
                            print(f'Data penumpang {nama} di kursi {nomor_kursi} berhasil dihapus!')
                            continue
                        else:
                            os.system('cls || clear')
                            print('Kursi tersebut memang sudah kosong!')
                            continue
                    else:
                        os.system('cls || clear')
                        print('Nomor kursi ' + tidakvalid())
                        continue
            
            elif input_admin == '3':
                os.system('cls || clear')
                break
                
            else:
                os.system('cls || clear')
                print(tidakvalid())
                continue

    # Akun User 
    elif input_nama == 'Nuron' and input_pw == '1234':
        os.system('cls || clear')
        
        login("USER")
        while not keluar:
            tampilkan_menu('USER')
            input_user = input(Input())

            if input_user == '1':
                os.system('cls || clear')
                print('TIKET YANG TERSEDIA:')
                print(f'1. {tujuan_penerbangan} [{jadwal_penerbangan}]')
                print('Penumpang yang sudah terdaftar: ')
                print(penumpang)
                input_user2 = input('KETIK 1 untuk keluar: ')
                if input_user2 == '1':
                    os.system('cls || clear')
                    continue
                else:
                    os.system('cls || clear')
                    print(tidakvalid())
                    continue

            elif input_user == '2':
                os.system('cls || clear')
                print(penumpang)
                beli_tiket()
                try:
                    nomor_kursi = int(input('Pilih nomor kursi yang ingin anda pilih: '))
                except ValueError:
                    os.system('cls || clear')
                    print(tidakvalid())
                    continue

                nama_penumpang = input('Masukkan Nama Penumpang: ')

                if 1 <= nomor_kursi <= maks_kursi:
                    if penumpang[nomor_kursi] == "":
                        penumpang[nomor_kursi] = nama_penumpang
                        os.system('cls || clear')
                        print('Tiket Berhasil Dipesan!')
                        continue
                    else:
                        os.system('cls || clear')
                        print('Maaf, kursi tersebut sudah terisi!')
                        continue
                else:
                    os.system('cls || clear')
                    print('Nomor kursi '+ tidakvalid() + ' Silakan pilih kursi yang tersedia.')
                    continue

            elif input_user == '3':
                os.system('cls || clear')
                print('Terima kasih telah berkunjung!')
                keluar = True

            else:
                os.system('cls || clear')
                print(tidakvalid())
                continue

    else:
        os.system('cls || clear')
        print(tidakvalid())

            


            

