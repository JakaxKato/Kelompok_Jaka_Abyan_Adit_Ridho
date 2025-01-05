import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi GUI Pertama")
root.geometry("400x300")  # Ukuran jendela: 400x300 piksel

# Tambahkan label
label = tk.Label(root, text="Halo, Selamat Datang di Tkinter!")
label.pack(pady=20)

# Jalankan aplikasi
root.mainloop()
