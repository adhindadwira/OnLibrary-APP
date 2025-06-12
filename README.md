# OnLibrary-APP
Laporan Tugas Besar Kode phyton beserta penjelasan aplikasi Perpustakaan Mini (On Library)

## Fitur Utama

* **Login Pengguna:** Membedakan akses antara administrator dan pengguna biasa.
    * **Admin:** Memiliki akses penuh ke penambahan, pengubahan, penghapusan, dan pencarian buku.
    * **Pengguna Biasa:** Dapat melakukan pencarian buku, peminjaman, dan pengembalian buku.
* **Pencarian Buku:** Cari buku berdasarkan kriteria tertentu. (Fitur terpisah: `pencarian.py`)
* **Manajemen Buku (Khusus Admin):**
    * **Penambahan Buku:** Menambahkan entri buku baru. (Fitur terpisah: `penambahan.py`)
    * **Pengubahan Buku:** Memperbarui detail buku yang sudah ada. (Fitur terpisah: `pengubahan.py`)
    * **Penghapusan Buku:** Menghapus buku dari sistem. (Fitur terpisah: `penghapusan.py`)
* **Peminjaman & Pengembalian Buku (Khusus Pengguna):**
    * **Peminjaman Buku:** Mencatat peminjaman buku oleh pengguna. (Fitur terpisah: `peminjaman.py`)
    * **Pengembalian Buku:** Mencatat pengembalian buku oleh pengguna. (Fitur terpisah: `pengembalian.py`)

# buku.xlsx - Sheet1.csv
* **Fungsi:** Berfungsi sebagai database penyimpanan data buku.
* **Detail:**
  * Ini adalah file CSV yang berisi semua informasi tentang buku-buku di perpustakaan, seperti judul, penulis, ISBN, jumlah stok, dll.
  * Semua operasi (penambahan, pengubahan, penghapusan, pencarian, peminjaman, pengembalian) akan membaca dan/atau menulis ke file ini.
  * (Catatan: Meskipun namanya menunjukkan Excel, .csv berarti itu adalah file teks terstruktur yang dipisahkan koma, yang umum digunakan untuk data sederhana.)

# main.py
* **Fungsi:** Merupakan entry point utama aplikasi. File ini menangani antarmuka login pengguna dan mengelola navigasi ke fitur-fitur lain berdasarkan hak akses (administrator atau pengguna biasa).
* **Detail:**
  * Menampilkan form login dengan input email dan password.
  * Memvalidasi kredensial login:
    * Jika email mengandung "@admin" dan password adalah "admin123", pengguna akan masuk sebagai administrator.
    * Jika email mengandung "@" (tanpa "@admin"), pengguna akan masuk sebagai pengguna biasa.
  * Setelah login berhasil, `main.py` akan menampilkan menu yang sesuai dengan peran pengguna dan menjalankan skrip Python terpisah untuk fitur yang dipilih menggunakan `subprocess.Popen`.

# peminjaman.py
* **Fungsi:** Mengelola proses peminjaman buku oleh pengguna.
* **Hak Akses:** Khusus Pengguna Biasa.
* **Detail:**
  * Modul ini memungkinkan pengguna untuk mencatat buku yang mereka pinjam.
  * Melibatkan pemilihan buku dan mungkin pencatatan tanggal peminjaman.

# penambahan.py
* **Fungsi:** Mengelola proses penambahan buku baru ke database perpustakaan.
* **Hak Akses:** Khusus Admin.
* **Detail:**
  * Modul ini menyediakan antarmuka untuk administrator memasukkan detail buku baru (misalnya, judul, penulis, ISBN, jumlah stok, dll.).
  * Setelah detail dimasukkan, data buku baru akan disimpan ke dalam database (kemungkinan buku.xlsx - Sheet1.csv).
  * Melakukan validasi input untuk memastikan data yang dimasukkan valid sebelum disimpan.

# pengubahan.py
8 **Fungsi:** Mengizinkan administrator untuk mengubah detail buku yang sudah ada dalam database perpustakaan.
* **Hak Akses:** Khusus Admin.
* **Detail:**
  * Administrator dapat mencari buku yang ingin diubah, lalu memodifikasi informasi seperti judul, penulis, ISBN, atau jumlah stok.
  * Perubahan akan diperbarui dalam database (kemungkinan buku.xlsx - Sheet1.csv).

# pencarian.py
* **Fungsi:** Menyediakan fungsionalitas untuk mencari buku dalam database perpustakaan.
* **Detail:**
  * Modul ini memungkinkan pengguna (baik admin maupun pengguna biasa) untuk mencari buku berdasarkan kriteria tertentu (misalnya, judul, penulis, ISBN, dll.).
  * Hasil pencarian biasanya ditampilkan dalam format tabel atau daftar yang mudah dibaca.
 
# pengembalian.py
* **Fungsi:** Mengelola proses pengembalian buku oleh pengguna.
* **Hak Akses:** Khusus Pengguna Biasa.
* **Detail:**
  * Modul ini memungkinkan pengguna untuk mencatat buku yang mereka kembalikan.
  * Memperbarui status atau stok buku menjadi tersedia kembali dalam database Anda.

# penghapusan.py 
* **Fungsi:** Bertanggung jawab untuk menghapus entri buku dari database perpustakaan.
* **Hak Akses:** Khusus Admin.
* **Detail:**
  * Administrator dapat memilih atau mencari buku yang ingin dihapus.
  * Setelah konfirmasi, data buku tersebut akan dihapus secara permanen dari database (kemungkinan buku.xlsx - Sheet1.csv).
  * Penting untuk menyertakan konfirmasi penghapusan untuk mencegah penghapusan yang tidak disengaja.
 
# sort.py
* **Fungsi:** Menyediakan fungsionalitas untuk mengurutkan daftar buku berdasarkan kriteria tertentu (misalnya, abjad judul, penulis, tahun terbit, dll.).
* **Detail:**
  * Modul ini dapat digunakan sebagai fitur terpisah atau terintegrasi dalam fitur pencarian/tampilan daftar buku untuk membantu pengguna menavigasi koleksi.

# UIUX.py
* **Fungsi:** Mungkin berisi elemen-elemen UI/UX yang dapat digunakan kembali atau konfigurasi tema untuk aplikasi.
* **Detail:**
Jika Anda memiliki fungsi atau kelas yang mengatur tampilan, gaya, atau komponen GUI yang sama di beberapa modul, maka uiux.py bisa menjadi tempat yang tepat untuk mengumpulkannya.
