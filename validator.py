nama_agen = input("Masukan Nama Agen:\n")
id_agen = int(input("Masukan ID Agen:\n"))
password_agen = input("Masukan Sandi Agen:\n")


def aku_butuh_validasi(nama, id_agen, sandi):
    if not nama:
        return False, "Nama gaboleh kosong"

    if not (1000 <= id_agen <= 9999):
        return False, "ID agen harus 4 digit angka."

    if len(sandi) < 8:
        return False, "sandi minimal 8 karakter."

    if "!" not in sandi and "?" not in sandi:
        return False, "Kata sandi harus ada karakter ! atau ?."

    return True, "Anjay valid."


akses, pesan = aku_butuh_validasi(
    nama_agen,
    id_agen,
    password_agen
)


if akses:
    print("helo world")
    print(pesan)
else:
    print("ditolak")
    print(pesan)
