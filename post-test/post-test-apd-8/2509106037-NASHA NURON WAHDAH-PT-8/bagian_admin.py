import os
from bagian_data import data
from bagian_fungsi import Input, tidakvalid, tampilkan_menu, tampilkan_tabel_penumpang, list_penumpang

def menu_admin(penumpang, maks_kursi):
    keluar = False
    while not keluar:
        tampilkan_menu('ADMIN_1')
        input_admin = input(Input())

        if input_admin == '1':
            os.system('cls || clear')
            list_penumpang()
            print('Jika kosong, berarti kursi belum terjual')
            print(tampilkan_tabel_penumpang(penumpang))
            input_admin2 = input('KETIK 1 untuk keluar: ')
            if input_admin2 == '1':
                continue
            else:
                print(tidakvalid())
                continue

        elif input_admin == '2':
            os.system('cls || clear')
            list_penumpang()
            print(tampilkan_tabel_penumpang(penumpang))
            tampilkan_menu('ADMIN_2')
            input_admin2 = input(Input())

            if input_admin2 == '1':
                os.system('cls || clear')
                print(tampilkan_tabel_penumpang(penumpang))
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
                print(tampilkan_tabel_penumpang(penumpang))
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
