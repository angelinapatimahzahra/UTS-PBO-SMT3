class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo Fajrin, nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya Fajrin")


mahasiswa = Mahasiswa()
mahasiswa.nama = "Angel"
mahasiswa.perkenalan()
mahasiswa.hello("Angel")
