# Import modul untuk GUI dan pengolahan file/data
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

# Import fungsi pencarian dan pengurutan
from search import sequential_search
from sort import bubble_sort

# Path file Excel
file_path = "buku.xlsx"

# Cek apakah file ada dan load data, jika tidak buat DataFrame kosong
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    df = pd.DataFrame(columns=["Kode Buku", "Judul Buku", "Penulis", "Kategori", "Tahun", "Status"])

df_sorted = pd.DataFrame(bubble_sort(df.to_dict("records"), key="Judul Buku"))

# Urutkan data berdasarkan judul buku
def balikin_buku():
    kode = kode_var.get().strip()  # Ambil kode dari input

    if not kode:
        messagebox.showwarning("Peringatan", "Masukkan Kode Buku terlebih dahulu.")
        return

    global df_sorted

    
    # Cari kode buku dengan sequential search
    list_kode = df_sorted["Kode Buku"].astype(str).tolist()
    idx = sequential_search(list_kode, kode)

    if idx == -1:
        messagebox.showerror("Peringatan", f"Buku tidak ditemukan. \nPastikan kode buku ditulis dengan benar! \n1. Gunakan huruf kapital \n2. Kode buku teridiri 4 Digit \nContoh : BK23")
        return

    status = str(df_sorted.iloc[idx]["Status"]).strip().lower()


    # Hanya bisa dikembalikan jika status "Dipinjam"
    if status == "dipinjam":
        df_sorted.at[idx, "Status"] = "Tersedia"
        try:
            df_sorted.to_excel(file_path, index=False)  # Simpan ke Excel
            messagebox.showinfo("Sukses", f"Buku '{df_sorted.iloc[idx]['Judul Buku']}' berhasil dikembalikan.")
            kode_var.set("") # Kosongkan Input
        except PermissionError:
            messagebox.showerror("Gagal", f"File '{file_path}' sedang dibuka. Tutup terlebih dahulu.")
    else:
        # JIka buku belum dipinjam
        messagebox.showwarning("Tidak Bisa", f"Buku tidak sedang dipinjam. Status saat ini: '{df_sorted.iloc[idx]['Status']}'.")

# GUI Setup
root = tk.Tk()
root.title("On Library (Pengembalian Buku)")
root.geometry("400x220")
root.configure(bg="white")

# Frame Utama
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x", expand=True)

# Variabel & Dropdown
kode_var = tk.StringVar()
daftar_kode = df_sorted["Kode Buku"].astype(str).tolist()

# Label dan Entry
ttk.Label(frame, text="Masukkan Kode Buku (4 Digit) :").pack(anchor="w", pady=5)
ttk.Entry(frame, textvariable=kode_var).pack(fill="x", pady=5)

# Tombol Pengembalian
ttk.Button(frame, text="Kembalikan Buku", command=balikin_buku).pack(pady=10)

# Jalankan GUI
root.mainloop()
