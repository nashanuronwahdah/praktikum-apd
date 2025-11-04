from prettytable import PrettyTable

# Fungsi Tanpa Parameter 
def Input():
    return "Masukkan Input(Hanya Angka): "

def tidakvalid():
    return "TIDAK VALID!"

# Fungsi Dengan Parameter 
def login(akun):
    print(f"ANDA BERHASIL LOGIN SEBAGAI {akun}!")
    
def tampilkan_menu(akun):
    if akun == 'ADMIN_1':
        print("SILAHKAN PILIH MENU YANG INGIN ANDA GUNAKAN:")
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
        
def tampilkan_tabel_penumpang(data_penumpang):
    table = PrettyTable(["Nomor Kursi", "Nama Penumpang"])
    for kursi, nama in data_penumpang.items():
        table.add_row([kursi, "KOSONG" if nama == "" else nama])
    return table
    
def list_penumpang():
    print('Berikut adalah list penumpang sesuai tempat duduk')
