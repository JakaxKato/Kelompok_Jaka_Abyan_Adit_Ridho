import os
import pandas as pd
from datetime import datetime

def tambah_tugas(tugas, nama, batas_waktu):
    try:
        batas_waktu = datetime.strptime(batas_waktu, "%Y-%m-%d %H:%M")
        tugas_baru = {"nama": nama, "batas_waktu": batas_waktu}
        tugas.append(tugas_baru)
        print(f"Tugas '{nama}' dengan batas waktu {batas_waktu} telah ditambahkan.")
    except ValueError:
        print("Format batas waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM.")

def tampilkan_tugas(tugas):
    if not tugas:
        print("Tidak ada tugas saat ini.")
    else:
        for i, tugas in enumerate(tugas, start=1):
            print(f"{i}. Tugas: {tugas['nama']} | Batas Waktu: {tugas['batas_waktu']}")

def hapus_tugas(tugas, indeks):
    if 1 <= indeks <= len(tugas):
        tugas_terhapus = tugas.pop(indeks - 1)
        print(f"Tugas '{tugas_terhapus['nama']}' telah dihapus.")
    else:
        print("Indeks tugas tidak valid.")

def simpan_ke_excel(tugas, nama_file="todolist.xlsx"):
    df = pd.DataFrame({"Nama Tugas": [tugas['nama'] for tugas in tugas], "Batas Waktu": [tugas['batas_waktu'] for tugas in tugas]})
    df.to_excel(nama_file, index=False)
    print(f"Tugas telah disimpan ke dalam file Excel '{nama_file}'.")

def baca_dari_excel(nama_file="todolist.xlsx"):
    tugas = []
    if os.path.exists(nama_file):
        df = pd.read_excel(nama_file)
        if 'Nama Tugas' in df.columns and 'Batas Waktu' in df.columns:
            for _, row in df.iterrows():
                tugas_baru = {"nama": row['Nama Tugas'], "batas_waktu": row['Batas Waktu']}
                tugas.append(tugas_baru)
        else:
            print("Format file Excel tidak sesuai. Pastikan kolom 'Nama Tugas' dan 'Batas Waktu' ada.")
    return tugas

def main():
    tugas = baca_dari_excel()

    while True:
        print("\n===== Aplikasi To-Do List =====")
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")

        pilihan = input("Pilih tindakan (1/2/3/4): ")

        if pilihan == "1":
            nama_tugas = input("Masukkan tugas baru: ")
            batas_waktu_tugas = input("Masukkan batas waktu tugas (format: YYYY-MM-DD HH:MM): ")
            tambah_tugas(tugas, nama_tugas, batas_waktu_tugas)
        elif pilihan == "2":
            tampilkan_tugas(tugas)
        elif pilihan == "3":
            tampilkan_tugas(tugas)
            indeks_hapus = int(input("Masukkan indeks tugas yang ingin dihapus: "))
            hapus_tugas(tugas, indeks_hapus)
        elif pilihan == "4":
            simpan_ke_excel(tugas)
            print("Aplikasi To-Do List ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
