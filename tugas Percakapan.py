import time

class PercakapanLiburan:
    # Class Attribute
    tujuan = "Liburan ke Dufan"
    hari = "Sabtu"

    # Constructor
    def __init__(self, nama):
        # Instance Attribute
        self.nama = nama

    # Method
    def berbicara(self, pesan):
        print(f"{self.nama}: {pesan}")


# Membuat Object
angel = PercakapanLiburan("Angel")
fajrin = PercakapanLiburan("Fajrin")


# Daftar Percakapan
percakapan = [
    (angel, "Hai Fajrin, apakah kamu punya rencana liburan?"),
    (fajrin, "Hai Angel, iya. Memangnya kamu mau ke mana?"),
    (angel, "Bagaimana kalau kita pergi liburan ke Dufan?"),
    (fajrin, "Wah, boleh banget. Saya juga ingin ke sana."),
    (angel, "Bagaimana kalau kita pergi hari Sabtu?"),
    (fajrin, "Saya setuju. Kita berangkat pagi saja."),
    (angel, "Nanti kita bisa mencoba berbagai macam wahana."),
    (fajrin, "Iya, saya ingin mencoba wahana Halilintar."),
    (angel, "Jangan lupa membeli tiket sebelum berangkat."),
    (fajrin, "Baik, nanti saya pesan tiketnya."),
    (angel, "Semoga liburan kita menyenangkan."),
    (fajrin, "Oke, sampai bertemu hari Sabtu!")
]


# Fungsi Menampilkan Percakapan
def tampilkan(delay=0.8):
    print("=== LIBURAN KE DUFAN ===")
    print("Tujuan:", PercakapanLiburan.tujuan)
    print("Hari:", PercakapanLiburan.hari)
    print("--------------------------------")

    for orang, teks in percakapan:
        orang.berbicara(teks)
        time.sleep(delay)

    print("--------------------------------")
    print("=== PERCAKAPAN SELESAI ===")


# Menjalankan Program
if __name__ == "__main__":
    tampilkan()
