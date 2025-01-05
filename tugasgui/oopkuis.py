"""
class Limas:
    def __init__(self, sisi, tinggi):
        self.sisi = sisi
        self.tinggi = tinggi

    def luas_permukaan(self):
        pass  

    def volume(self):
        pass  

class Segitiga(Limas):
    def __init__(self, sisi, tinggi, sisi_miring):
        super().__init__(sisi, tinggi)
        self.sisi_miring = sisi_miring

    def luas_permukaan(self):
        return (1/2) * self.sisi * self.tinggi + 3 * ((1/2) * self.sisi * self.sisi_miring)

    def volume(self):
        return (1/3) * (1/2) * self.sisi * self.tinggi * self.sisi_miring

class SegiEmpat(Limas):
    def __init__(self, sisi, tinggi, sisi_miring):
        super().__init__(sisi, tinggi)
        self.sisi_miring = sisi_miring

    def luas_permukaan(self):
        return self.sisi * self.tinggi + 4 * ((1/2) * self.sisi * self.sisi_miring)

    def volume(self):
        return (1/3) * self.sisi * self.tinggi * self.sisi_miring

class SegiEnam(Limas):
    def __init__(self, sisi, tinggi, sisi_miring):
        super().__init__(sisi, tinggi)
        self.sisi_miring = sisi_miring

    def luas_permukaan(self):
        return 3 * (1/2) * self.sisi * self.sisi_miring + 6 * ((1/2) * self.sisi * self.tinggi)

    def volume(self):
        return (1/3) * (1/2) * self.sisi * self.tinggi * self.sisi_miring

def main():
    sisi = float(input("Masukkan panjang sisi: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi_miring = float(input("Masukkan panjang sisi miring: "))

    limas_segitiga = Segitiga(sisi, tinggi, sisi_miring)
    limas_segiempat = SegiEmpat(sisi, tinggi, sisi_miring)
    limas_segienam = SegiEnam(sisi, tinggi, sisi_miring)

    print("\nLuas Permukaan dan Volume Limas Segitiga:")
    print(f"Luas Permukaan: {limas_segitiga.luas_permukaan()}")
    print(f"Volume: {limas_segitiga.volume()}")

    print("\nLuas Permukaan dan Volume Limas Segiempat:")
    print(f"Luas Permukaan: {limas_segiempat.luas_permukaan()}")
    print(f"Volume: {limas_segiempat.volume()}")

    print("\nLuas Permukaan dan Volume Limas Segienam:")
    print(f"Luas Permukaan: {limas_segienam.luas_permukaan()}")
    print(f"Volume: {limas_segienam.volume()}")


hasil = main()
print(hasil)

"""
"""
class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def display_data(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("IPK:", self.ipk)

class ManajemenMahasiswa:
    def __init__(self):
        self.mahasiswas = []

    def input_data_mahasiswa(self):
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        ipk = float(input("Masukkan IPK mahasiswa: "))
        mahasiswa = Mahasiswa(nama, nim, ipk)
        self.mahasiswas.append(mahasiswa)
        print("Data mahasiswa berhasil ditambahkan.")

    def display_data_mahasiswa(self):
        if not self.mahasiswas:
            print("Belum ada data mahasiswa.")
        else:
            print("Data Mahasiswa:")
            for mahasiswa in self.mahasiswas:
                mahasiswa.display_data()
                print()

    def search_data_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswas:
            if mahasiswa.nim == nim:
                mahasiswa.display_data()
                return mahasiswa
        print(f"Tidak ditemukan data mahasiswa dengan NIM {nim}.")
        return None

    def delete_data_mahasiswa(self, nim):
        mahasiswa = self.search_data_mahasiswa(nim)
        if mahasiswa:
            self.mahasiswas.remove(mahasiswa)
            print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")

    def update_data_mahasiswa(self, nim):
        mahasiswa = self.search_data_mahasiswa(nim)
        if mahasiswa:
            print(f"Masukkan data baru untuk mahasiswa dengan NIM {nim}:")
            new_nama = input("Nama baru: ")
            new_nim = input("NIM baru: ")
            new_ipk = float(input("IPK baru: "))
            mahasiswa.nama = new_nama
            mahasiswa.nim = new_nim
            mahasiswa.ipk = new_ipk
            print(f"Data mahasiswa dengan NIM {nim} berhasil diperbarui.")

# Program Utama
manajemen = ManajemenMahasiswa()

while True:
    print("\nMenu:")
    print("1. Input Data Mahasiswa")
    print("2. Display Data Mahasiswa")
    print("3. Search Data Mahasiswa")
    print("4. Delete Data Mahasiswa")
    print("5. Update Data Mahasiswa")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        manajemen.input_data_mahasiswa()
    elif pilihan == '2':
        manajemen.display_data_mahasiswa()
    elif pilihan == '3':
        nim_cari = input("Masukkan NIM Mahasiswa yang dicari: ")
        manajemen.search_data_mahasiswa(nim_cari)
    elif pilihan == '4':
        nim_hapus = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
        manajemen.delete_data_mahasiswa(nim_hapus)
    elif pilihan == '5':
        nim_update = input("Masukkan NIM Mahasiswa yang akan diperbarui: ")
        manajemen.update_data_mahasiswa(nim_update)
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")
"""
from bs4 import BeautifulSoup as bs
import requests

req = requests.get("https://id.wikipedia.org/wiki/Cristiano_Ronaldo")
soup = bs(req.content, "html.parser")
infobox = soup.find("table", {'class': 'infobox biography vcard'})

informasi = {}

if infobox:
    for indata in infobox.find_all('tr')[2:]:
        try:
            judul = indata.find('th').get_text()
            info = indata.find('td').get_text()
            informasi[judul] = info
        except AttributeError:
            # Handle the case where either 'th' or 'td' is not found in the row
            pass

for key, value in informasi.items():
    print(key, "=", value)
