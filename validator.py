nama = input("Masukan Nama: ")
id = input("Masukan ID: ")
sandi = input("Sandi: ")

def validasi(nama, id, sandi):
    if not nama.strip():
        return False, "Nama kosong"
    if not id.isdigit() or not 1000 <= int(id) <= 9999:
        return False, "ID harus 4 digit"
    if len(sandi) < 8 or ("!" not in sandi and "?" not in sandi):
        return False, "Sandi tidak valid"
    return True, "Valid"

hasil = validasi(nama, id, sandi)

if hasil[0]:
    print("AKSES DITERIMA")
else:
    print("AKSES DITOLAK")
print(hasil[1])
