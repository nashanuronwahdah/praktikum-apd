# for i in range (10):
#     print (i + 1)

# nama = ['Bakil', 'Diftya', 'Anugrah']
# for i in nama:
#     print(i)



# for j in range(3):
#     print('Raffi')



# while loop 
# jawab = 'ya'
# hitung = 0

# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input('ulangi lagi? :')

# print(f'total jawab ya {hitung}')



# cuaca = 'hujan'

# while (cuaca == 'hujan' or cuaca == 'Hujan'):
#     print('Jangan keluar rumah')
#     cuaca = input('Apa cuaca saat ini: ')

# print('keluar ruumah')



# angka = 10

# while ( angka > 1):
#     print(angka)
#     angka -= 2


# for i in range (1, 5):
#     for j in range(1,5):
#         print(f'{i} x {j} = {i * j}')
#     print()


# break 

# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")

# for i in angka:
#     print(f"Sekarang memeriksa angka: {i}")
#     if i > 10:
#             print(f"Angka {i} lebih besar dari 10, Perulangan berhenti.")
#             break

# print("Program selesai.")


# continue 
# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print(f"Angka genap ditemukan: {i}")

# print("\nProgram selesai.")


# contoh list comprehension
# kuadrat = [i**2 for i in range(1, 5)]
# print(kuadrat)

# pembanding
# for i in range(1,5):
#     print(i**2)


# angka_genap = [x for x in range(1, 11) if x%2==0]
# print(angka_genap)

# for x in range(1,11):
#     if x%2==0:
#         print(x)


# angka_ganjil = [x for x in range(1,12) if x%2 != 0]
# print(angka_ganjil)


for i in range (1,6):
     print('*' * (6 - i))
