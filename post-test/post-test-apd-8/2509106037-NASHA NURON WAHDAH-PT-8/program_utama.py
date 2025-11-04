import os
from bagian_data import data
from bagian_admin import menu_admin
from bagian_user import menu_user
from bagian_fungsi import login
admin, pw1, user, pw2, penumpang, tujuan_penerbangan, jadwal_penerbangan, maks_kursi = data()


while True:

    print('SELAMAT DATANG DI PENERBANGAN FUFUFAFA-AIR')
    print('SILAHKAN LOGIN SESUAI AKUN ANDA')
    input_nama = input('Silahkan Masukkan Username anda: ')
    input_pw = input('Silahkan Masukkan Password anda: ')

    # Akun Admin 
    if input_nama == admin and input_pw == pw1:
        os.system('cls || clear')
        login('ADMIN')
        menu_admin(penumpang, maks_kursi)

    # Akun User 
    elif input_nama == user and input_pw == pw2:
        os.system('cls || clear')
        login("USER")
        menu_user(penumpang, maks_kursi, tujuan_penerbangan, jadwal_penerbangan)

    else:
        os.system('cls || clear')
        print('TIDAK VALID!')
