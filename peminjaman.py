# Import Modul untuk GUI dan Pengolahan Data
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

# Import algoritma pencarian dan pengurutan
from search import sequential_search
from sort import bubble_sort

# Path file Excel yang digunakan
file_path = "buku.xlsx"

# Cek apakah file ada, jika tidak buat DataFrame kosong
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    df = pd.DataFrame(columns=["Kode Buku", "Judul Buku", "Penulis", "Kategori", "Tahun", "Status"])

# Bubble sort berdasarkan Judul Buku (opsional jika ingin lihat urutan)
df_sorted = pd.DataFrame(bubble_sort(df.to_dict("records"), key="Judul Buku"))

# Fungsi peminjaman buku
def pinjam_buku():
    kode = kode_var.get().strip()

    if not kode:
        messagebox.showwarning("Peringatan", "Masukkan Kode Buku terlebih dahulu.")
        return

    global df_sorted

    # Ambil daftar kode buku dan cari indeksnya dengan sequential search
    list_kode = df_sorted["Kode Buku"].astype(str).tolist()
    idx = sequential_search(list_kode, kode)

    if idx == -1:
        messagebox.showerror("Peringatan", f"Buku tidak ditemukan. \nPastikan kode buku ditulis dengan benar! \n1. Gunakan huruf kapital \n2.Kode buku teridiri 4 Digit \nContoh : BK23")
        return

    # Cek status buku (tersedia atau tidak)
    status = df_sorted.iloc[idx]["Status"]

    if status.lower() == "tersedia":
        df_sorted.at[idx, "Status"] = "Dipinjam"
        try:
            df_sorted.to_excel(file_path, index=False)
            messagebox.showinfo("Berhasil", f"Buku '{df_sorted.iloc[idx]['Judul Buku']}' berhasil dipinjam.")
            kode_var.set("")
        except PermissionError:
            messagebox.showerror("Gagal", f"File '{file_path}' sedang dibuka. Tutup terlebih dahulu.")
    else:
        messagebox.showwarning("Tidak Tersedia", f"Buku '{df_sorted.iloc[idx]['Judul Buku']}' sedang {status.lower()}.")

# GUI Setup
root = tk.Tk()
root.title("Peminjaman Buku")
root.geometry("400x200")
root.configure(bg="white")

# Buat frame utama
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x", expand=True)

# Variabel input untuk kode buku
kode_var = tk.StringVar()

# Label dan Entry
ttk.Label(frame, text="Masukkan Kode Buku (4 Digit):").pack(anchor="w", pady=5)
ttk.Entry(frame, textvariable=kode_var).pack(fill="x", pady=5)

# Tombol Peminjaman
ttk.Button(frame, text="Pinjam Buku", command=pinjam_buku).pack(pady=10)

# Jalankan GUI
root.mainloop()
