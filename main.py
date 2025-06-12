# Import modul Tkinter dan utilitas lainnya
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess # untuk menjalankan file eksternal .py

# Fungsi untuk menjalankan file python lain (fitur terpisah)
def jalankan(file): subprocess.Popen(["python", file])

# Fungsi untuk menampilkan menu utama setelah login
def tampilkan_menu(fitur_lengkap=False, user_mode=False):
    for widget in root.winfo_children(): widget.destroy()  # Hapus semua elemen GUI sebelumnya

    # Buat frame tengah untuk tampilan menu
    frame = tk.Frame(root, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Judul Menu
    tk.Label(frame, text="Pilih Fitur", font=("Arial", 14, "bold")).pack(pady=10)
    ttk.Button(frame, text="Pencarian Buku", width=30, command=lambda: jalankan("pencarian.py")).pack(pady=5)

    # Menu Khusus Admin
    if fitur_lengkap:
        ttk.Button(frame, text="Penambahan Buku", width=30, command=lambda: jalankan("penambahan.py")).pack(pady=5)
        ttk.Button(frame, text="Pengubahan Buku", width=30, command=lambda: jalankan("pengubahan.py")).pack(pady=5)
        ttk.Button(frame, text="Penghapusan Buku", width=30, command=lambda: jalankan("penghapusan.py")).pack(pady=5)
    # Menu Khusus Pengguna Biasa 
    elif user_mode:
        ttk.Button(frame, text="Peminjaman Buku", width=30, command=lambda: jalankan("peminjaman.py")).pack(pady=5)
        ttk.Button(frame, text="Pengembalian Buku", width=30, command=lambda: jalankan("pengembalian.py")).pack(pady=5)

# Fungsi Login, Membedakan Admin dan User Biasa 
def login():
    email = email_var.get().lower()
    pwd = pass_var.get()

    if "@admin" in email:
        if pwd == "admin123":
            tampilkan_menu(fitur_lengkap=True)
        else:
            messagebox.showerror("Login Gagal", "Password admin salah.")
    elif "@" in email:
        tampilkan_menu(user_mode=True)
    else:
        messagebox.showwarning("Input Tidak Valid", "Masukkan email yang valid.")

# Setup GUI Login
root = tk.Tk()
root.title("On Library")
root.geometry("400x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Judul Aplikasi
tk.Label(frame, text="On Library", font=("Arial", 14, "bold")).pack(pady=10)
email_var = tk.StringVar()
pass_var = tk.StringVar()

# Input Nilai
ttk.Label(frame, text="Email:").pack(anchor="w")
ttk.Entry(frame, textvariable=email_var).pack(fill="x")

# Input Password 
ttk.Label(frame, text="Password:").pack(anchor="w")
ttk.Entry(frame, textvariable=pass_var, show="*").pack(fill="x")

# Tombol Login 
ttk.Button(frame, text="Login", command=login).pack(pady=15)

# Jalankan GUI
root.mainloop()
