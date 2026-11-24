class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim):  # Manual setup
        self.nama = nama
        self.nim = nim


# Harus panggil setup manual
mhs = Mahasiswa("Alice", "123456")
print(mhs.nama)
print(mhs.nim)


class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        # validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.no = no
        self.saldo = saldo


budi = BankAccount("1234567890", 1000)  # sukses
print(budi.no)
print(budi.saldo)

# Contoh error
try:
    eko = BankAccount("1234567890", -1000)
except ValueError as e:
    print(e)
