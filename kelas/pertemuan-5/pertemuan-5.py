# membuat list 
# matakuliah = ['APD', 'Kalkulus', 'Orsikom']

# matakuliah = []

# membaca list 
# print(matakuliah[1 : 3])

# # dari belakang
# print(matakuliah[-1])

# print(matakuliah[1:3:2])

# matakuliah.append('Matematika')

# matakuliah.insert(2, 'Matematika')

# print(matakuliah)

# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(praktikum[4][0])

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# studyclub.append("Web")
# print(studyclub)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# menghapus sesuai indeks
# del matakuliah[2]

# menghapus sesuai isi dari indeksnya
# matakuliah.remove('Kalkulus')

# ngehapus indeks terakhir, pop itu bisa disimpan di dalam variabel
# matakuliah.pop(3)

# hapus = matakuliah.pop(3)

# print(matakuliah)
# print(hapus)

# list= [1, 2, 3]

# len, sum, min 
# print (len(list))

# list = ['1', '2', '3']
# nilai = ['4', '5', '6']

# hasil = list + nilai
# kali = (list+nilai)*3
# print(hasil)
# print(kali)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# for index, i in enumerate(matakuliah):
#     print(index, i)

# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# # print(kelas[0] [0]) 

# # kelas[1].insert(1, 'matematika')
# # print(kelas)

# # kalau mau print kebawah
# for i in kelas:
#    for a in i:
#       print(a)

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota [4] [0])

studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy=list(studyclub)

liststudy[1] = 'Web'

print(f'Ini tuple :' (studyclub))