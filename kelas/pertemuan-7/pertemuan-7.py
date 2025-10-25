# # def halo():
# #     print('Halo Guys!')

# # halo()

# # def luas_persegi_panjang(panjang, lebar):
# #     luas = panjang * lebar
# #     print ('luas persegi panjang adalah' , luas)

# # luas_persegi_panjang(4, 5)

# # # luas itu berfungsi menyimpan rumus saja, return mengembalikan hasil operasi ke print(pemanggilan )
# # def luas_persegi(sisi):
# #     luas = sisi * sisi
# #     return luas

# # print ("Luas persegi :", luas_persegi(8))

# # # rumus: sisi x sisi
# # def luas_persegi(sisi):
# #     luas = sisi * sisi
# #     return luas
# # # rumus: sisi x sisi x sisi
# # def volume_persegi(sisi):
# #     volume = luas_persegi(sisi) * sisi
# #     print ("Volume Persegi = ", volume)

# # # pemanggilan Fungsi
# # luas_persegi(4)
# # volume_persegi(6)

# # nama = 'Ridho'

# # def LuasPersegiPanjang(panjang, lebar):
# #     luas = panjang * lebar
# #     return luas

# # print(LuasPersegiPanjang(2, 6))

# # def luas_segitiga(alas, tinggi):
# #     luas = 1/2 * alas * tinggi
# #     return luas

# # print(luas_segitiga(2, 5))

# # nama = 'ridho'

# # def biodata():
# #     username = 'nabil'
# #     print(username)
# # biodata()

# # def faktorial(n):
# #     if n==1 or n==0:
# #         return 1
# #     else:
# #         return n * faktorial(n-1)
    
# # print(faktorial(5))



# film = []


# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks+1, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")


# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")


# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")


# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# if __name__ == "_main_":
#         while (True):
#             show_menu()

# print(show_menu())


# # try:
# #     angka = int(input('Masukkan Angka: '))
# # except ValueError:
# #     print("Angka Tidak Boleh String!")
