nama_agen = input("Masukan nama agen: ")
id_agen = int(input("Masukan ID agen: "))
kata_sandi = input("Masukan kata sandi: ")

def validate_access(name, id_number, passcode):
    if name == "":
        return False, "nama tidak boleh kosong"

    if not (1000 <= id_number <= 9999):
        return False, "ID harus berisi 4 digit"
    if id_number =="":
        return False, "nama tidak boleh ksong"

    if len(passcode) < 8:
        return False, "password harus berisi 8 digit"

    if "!" not in passcode and "?" not in passcode:
        return False,"Password harus berisikan karakter ! ?"
    return True, "Valid"
validate_access(nama_agen, id_agen, kata_sandi)
print(validate_access(nama_agen, id_agen, kata_sandi))
