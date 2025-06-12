# Mengimpor modul Image dan ImageTk dari pustaka PIL (Pillow) untuk manipulasi gambar
from PIL import Image, ImageTk
import tkinter as tk    # Mengimpor pustaka tkinter untuk membuat antarmuka pengguna grafis (GUI)

# Warna & font
warna_bg = "#ffffff"   # Mendefinisikan variabel warna_bg dengan kode heksadesimal untuk warna putih
font_judul = ("Segoe Script", 16, "bold")

# Gambar background
path_bg = "BgLogin.png"

# Mendefinisikan fungsi pasang_background yang menerima argumen 'root' (biasanya jendela utama tkinter)
def pasang_background(root):
    try:
        img = Image.open(path_bg)
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        bg = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=bg)
        label.image = bg  # simpan referensi
        label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Gagal pasang background: {e}")
