# data.py

def data():
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

    # Variabel Global
    tujuan_penerbangan = "SAMARINDA TO DIDDY ISLAND"
    jadwal_penerbangan = "BESOK 17.30"
    maks_kursi = 6

    return admin, pw1, user, pw2, penumpang, tujuan_penerbangan, jadwal_penerbangan, maks_kursi
