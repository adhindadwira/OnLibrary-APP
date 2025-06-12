# Import GUI, pengolahan data, dan pencarian teks
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import difflib   # untuk rekomendasi teks mirip

# Import algoritma pencarian dan pengurutan
from search import sequential_search
from sort import bubble_sort

# Coba load data dari file Excel, jika gagal buat kosong
try:
    df = pd.read_excel("buku.xlsx")
except FileNotFoundError:
    df = pd.DataFrame()

# Inisialisasi window
app = tk.Tk()
app.title("Cari Buku")
app.geometry("900x600")

# Variabel pilihan dan input
pilihan = tk.StringVar()
input_pencarian = tk.StringVar()

# Fungsi untuk menampilkan hasil pencarian
def tampilkan_hasil(hasil_list, rekomendasi=False):
    if not hasil_list:
        pesan = "Buku tidak ditemukan! \nPeriksa kembali ejaan atau coba kata kunci lain."
    else:
        hasil_list = bubble_sort(hasil_list, key="Judul Buku")
        pesan = "Rekomendasi buku yang mungkin Anda maksud:\n\n" if rekomendasi else ""
        for buku in hasil_list:
            pesan += (
                f"Judul : {buku['Judul Buku']}\n"
                f"Kode  : {buku['Kode Buku']}\n"
                f"Penulis: {buku['Penulis']}\n"
                f"Kategori: {buku['Kategori']}\n"
                f"Tahun : {buku['Tahun']}\n"
                f"Status: {buku['Status']}\n\n"
            )
    messagebox.showinfo("Hasil Pencarian", pesan)

# Fungsi pencarian dari input teks menggunakan sequential search
def cari_dari_input():
    kunci = input_pencarian.get().strip()
    kolom = pilihan.get()

    if kolom and kunci:
        data_list = df[kolom].astype(str).tolist()
        index_ditemukan = sequential_search(data_list, kunci)

        if index_ditemukan != -1:
            hasil = [df.loc[index_ditemukan].to_dict()]
            tampilkan_hasil(hasil)
        else:
            kunci_lower = kunci.lower()
# Ambil 3 kemiripan terdekat dari kolom yang dipilih
        hasil_mirip = difflib.get_close_matches(kunci_lower, [str(item).lower() for item in data_list], n=3, cutoff=0.5)
        rekomendasi = []
        for i, item in enumerate(data_list):
            if str(item).lower() in hasil_mirip:
                rekomendasi.append(df.loc[i].to_dict())

        tampilkan_hasil(rekomendasi, rekomendasi=True)

# Fungsi pencarian dari tombol kategori/tahun (exact match)
def cari_dari_tombol(nilai):
    kolom = pilihan.get()
    hasil_df = df[df[kolom].astype(str) == str(nilai)]
    tampilkan_hasil(hasil_df.to_dict("records"))

# Fungsi untuk membuat ulang input atau tombol berdasarkan pilihan dropdown
def ubah_pilihan(*args):
    for widget in frame_input.winfo_children():
        widget.destroy()

    kolom = pilihan.get()

    if kolom in ["Judul Buku", "Kode Buku", "Penulis"]:
        ttk.Label(frame_input, text=f"Masukkan {kolom}:").pack()
        ttk.Entry(frame_input, textvariable=input_pencarian).pack(fill='x', padx=5)
        ttk.Button(frame_input, text="Cari", command=cari_dari_input).pack(pady=5)

    elif kolom in ["Kategori", "Tahun"]:
        nilai_unik = df[kolom].dropna().unique()
        nilai_unik.sort()

        canvas = tk.Canvas(frame_input)
        scrollbar = ttk.Scrollbar(frame_input, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for val in nilai_unik:
            ttk.Button(scrollable_frame, text=str(val), command=lambda v=val: cari_dari_tombol(v)).pack(fill='x', padx=5, pady=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

# Container tengah
container = ttk.Frame(app)
container.place(relx=0.5, rely=0.5, anchor="center")

# Frame dropdown
frame_dropdown = ttk.Frame(container)
frame_dropdown.pack(pady=10, fill='x')
ttk.Label(frame_dropdown, text="Pilih Kolom Pencarian:").pack()
dropdown = ttk.Combobox(frame_dropdown, textvariable=pilihan, state="readonly")
dropdown['values'] = ["Judul Buku", "Kode Buku", "Penulis", "Kategori", "Tahun"]
dropdown.pack(fill='x', padx=5)
pilihan.trace('w', ubah_pilihan)

# Frame untuk input
frame_input = ttk.Frame(container)
frame_input.pack(fill='both', expand=True, padx=10, pady=10)

# Jalankan GUI
app.mainloop()
