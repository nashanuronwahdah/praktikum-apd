# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "Daffa"}
# }

# for i, j in Biodata.items():
#     print(i)
#     print(j)

# for i in Biodata:
#     for a in i:
#         print(i)

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Alamat"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror",
# }

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})

# del Film["Avenger Endgame"]
# print(Film)

# for i in Film:
#     print(i)

Musik = {
    "The Chainsmoker": ["All we Know", "The Paris"],
    "Alan Walker": ["Alone", "Lily"],
    "Neffex": ["Best of Me",['tes','halo'], "Memories"],
    'Paramore' : ["Misery Business", "Ain't It Fun", 
                ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
}

print(Musik['Paramore'][2][1][0])