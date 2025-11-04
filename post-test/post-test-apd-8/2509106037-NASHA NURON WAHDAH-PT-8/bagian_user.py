import os
from bagian_data import data
from bagian_fungsi import Input, tidakvalid, tampilkan_menu, tampilkan_tabel_penumpang

def menu_user(penumpang, maks_kursi, tujuan_penerbangan, jadwal_penerbangan):
    keluar = False
    while not keluar:
        tampilkan_menu('USER')
        input_user = input(Input())

        if input_user == '1':
            os.system('cls || clear')
            print('TIKET YANG TERSEDIA:')
            print(f'1. {tujuan_penerbangan} [{jadwal_penerbangan}]')
            print('Penumpang yang sudah terdaftar: ')
            print(tampilkan_tabel_penumpang(penumpang))
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
            print(tampilkan_tabel_penumpang(penumpang))
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
