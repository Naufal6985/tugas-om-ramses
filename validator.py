nama_agen = input("Masukan nama agen: ")
id_agen = input("Masukan ID agen: ")
kata_sandi = input("Masukan kata sandi: ")

def validate_access(name, id_agen, passcode):
    output = []
    if name == "":
        output.append("Nama tidak boleh kosong")
    if id_agen == "":
        output.append("ID tidak boleh kosong")
    else:
        id_agen = int(id_agen)
        if not (1000 <= id_agen <= 9999):
            output.append("ID harus berisi 4 digit")
    if len(passcode) < 8:
        output.append("Password harus minimal 8 karakter")
    if "!" not in passcode and "?" not in passcode:
        output.append("Password harus mengandung ! atau ?")
    if output:
        return False, "\n".join(output)
    return True, "Valid"
print(validate_access(nama_agen, id_agen, kata_sandi)[1])
