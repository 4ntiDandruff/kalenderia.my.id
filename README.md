# 📅 Kalenderia.my.id — Website Workshop Percetakan Kalender 2027 (Sidoarjo)

**Kalenderia.my.id** adalah platform katalog interaktif & penawaran B2B percetakan kalender presisi berbasis di Workshop Candi, Sidoarjo (Tahun Aktif Produksi: **2027**). Dibangun dengan arsitektur **Clean Light Workshop**, menggabungkan kecepatan **Python Flask**, keindahan **Tailwind CSS v4 Standalone**, interaktivitas seamless **HTMX**, serta gambar mockup fisik realistis resolusi tinggi hasil render Pillow (PIL).

---

## 🖥️ PANDUAN LENGKAP PENGGUNA WINDOWS (SANGAT AWAM & PEMULA)

Bagi Anda pengguna Windows (Windows 10 / Windows 11) yang belum pernah coding atau belum pernah menggunakan Command Line, gunakan panduan langkah-demi-langkah super simpel di bawah ini:

---

### 📥 Langkah 1: Download & Install Python (Wajib Centang PATH)

1. Buka Google Chrome / Microsoft Edge, masuk ke halaman resmi: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Klik tombol kuning **"Download Python 3.12"** (atau versi terbaru).
3. Buka file **`python-3.12.x-amd64.exe`** di folder Downloads Anda.
4. ⚠️ **LANGKAH PALING KRUSIAL**:
   - Di bagian bawah jendela installer pertama, **CENTANG / CHECKLIST** kotak tulisan:
     `[✓] Add python.exe to PATH`
5. Setelah dicentang, klik tombol **"Install Now"** di bagian atas.
6. Tunggu proses instalasi selesai sampai muncul teks *Setup was successful*, lalu klik **Close**.

---

### 📦 Langkah 2: Download Project dari GitHub

#### Cara Paling Mudah (Tanpa Install Git):
1. Buka halaman GitHub project ini: **[https://github.com/4ntiDandruff/kalenderia.my.id](https://github.com/4ntiDandruff/kalenderia.my.id)**
2. Klik tombol hijau tulisan **`<> Code`** di sebelah kanan atas.
3. Klik opsi **`Download ZIP`**.
4. Buka folder Downloads Anda, klik kanan file **`kalenderia.my.id-main.zip`**, lalu pilih **Extract All...** (Ekstrak Semua).
5. Simpan di lokasi yang mudah ditemukan, misalnya di **`C:\kalenderia.my.id`** atau di **`Desktop`**.

---

### 🚀 Langkah 3: Menjalankan Aplikasi di Windows (Metode 1-Klik Otomatis)

Project ini sudah dilengkapi file script otomatis bernama **`run_windows.bat`**. Anda tidak perlu mengetik perintah apapun!

1. Buka folder hasil ekstrak project tadi (folder yang berisi file `app.py`, `README.md`, dll).
2. Cari file bernama **`run_windows.bat`** (berikon gerigi/batch file).
3. **Klik 2x (Double-click)** pada file `run_windows.bat` tersebut.
4. Jendela Command Prompt hitam akan terbuka dan secara otomatis melakukan:
   - Setup Virtual Environment (`venv`)
   - Menginstall Flask & modul gambar Pillow secara otomatis
   - Mengisi database awal (`kalenderia.db`)
   - Meng-generate seluruh gambar produk PNG realistis di folder `static/images/real/`
   - Menjalankan server aplikasi lokal.
5. Setelah muncul tulisan `Running on http://127.0.0.1:5005`, buka browser (Chrome / Edge) lalu masuk ke alamat:
   👉 **`http://localhost:5005`** atau **`http://127.0.0.1:5005`**

---

### 💻 Langkah 4: Cara Menjalankan Manual via Command Prompt (CMD)

Jika Anda ingin menjalankan secara manual via CMD Windows:

1. Tekan tombol `Windows + R` di keyboard, ketik **`cmd`**, lalu tekan **Enter**.
2. Masuk ke folder project, contoh:
   ```cmd
   cd C:\kalenderia.my.id
   ```
3. Buat dan aktifkan Virtual Environment Python:
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```
   *(Akan muncul penanda `(venv)` di sebelah kiri prompt CMD)*
4. Install library yang dibutuhkan:
   ```cmd
   pip install -r requirements.txt
   ```
5. Siapkan database & gambar sampel:
   ```cmd
   python init_db.py
   python generate_real_png.py
   ```
6. Jalankan server web:
   ```cmd
   python app.py
   ```
7. Buka browser Anda di **`http://localhost:5005`**.

---

### ❓ Pertanyaan & Pertolongan Pertama (FAQ Kendala Windows)

* **Tanya: Muncul pesan error `'python' is not recognized as an internal or external command`**
  * **Jawab**: Ini artinya Anda lupa mencentang *"Add python.exe to PATH"* saat install Python di Langkah 1. Jalankan lagi installer Python Anda, pilih *Modify* / *Reinstall*, dan pastikan centang opsi *Add python.exe to PATH*.

* **Tanya: Bagaimana cara mematikan / menghentikan server jika sudah selesai dipakai?**
  * **Jawab**: Cukup tutup jendela CMD hitam tersebut, atau tekan kombinasi tombol **`Ctrl + C`** di keyboard saat berada di jendela CMD.

* **Tanya: Apakah butuh koneksi internet saat menjalankan website di komputer lokal?**
  * **Jawab**: Tidak butuh! Setelah langkah instalasi selesai, aplikasi web Kalenderia dapat dijalankan 100% secara offline di PC/laptop Windows Anda.

---

## 🛠️ Tech Stack & Ekosistem

- **Backend Framework**: Python 3.10+ / Flask (dengan helper interseptor `is_hx_request()`)
- **Database Layer**: SQLite 3 (`kalenderia.db`) disemai via `init_db.py`
- **Frontend Engine**: Jinja2 Templates + HTMX v1.9.10 (Single-Page Experience partial swap)
- **UI Design System**: Tailwind CSS v4 Standalone (Clean Light Workshop & Emerald Palette `#10b981`)
- **Asset Mockup Generator**: Python Pillow (PIL) `generate_real_png.py` untuk gambar fisik PNG realistis
- **Process Manager**: PM2 / Gunicorn / Windows Batch Launcher (`http://127.0.0.1:5005`)

---

## 📋 Fitur Utama & Keunggulan B2B

1. **Clean Light Workshop & Mobile Off-Canvas Drawer**:
   - Tampilan ultra-clean dengan canvas `bg-slate-50`, card `bg-white`, dan aksen primer Emerald (`bg-emerald-600`).
   - Fitur Mobile Navigation Drawer melayang dengan backdrop blur di bawah breakpoint `lg:`, serta persistent sticky sidebar di desktop (`lg:block`).
2. **Animasi & Mikro-Interaksi Performa Tinggi (GPU-Accelerated)**:
   - Efek `card-hover-lift` (`-4px` translate + soft shadow) pada seluruh produk, template, dan bento box.
   - Feedback tekan `active-press` (`active:scale-95`) pada tombol CTA WhatsApp dan filter tab.
   - Smooth `animate-fade-in` pada container `#main-content` saat swap HTMX.
3. **Gambar Mockup Fisik Realistis High-Res**:
   - Seluruh produk, template, dan bahan kertas menggunakan gambar render fisik PNG (`/static/images/real/*.png`) resolusi tinggi tanpa SVG kusam.
4. **Navigasi Active State Auto-Manager**:
   - `static/main.js` mengelola kelas status aktif sidebar secara presisi berbasis `window.location.pathname` yang terintegrasi dengan event HTMX (`htmx:afterSwap`, `htmx:historyRestore`).
5. **Kaya Nilai B2B Trust-Centric**:
   - Fitur Promo Pre-Order 2027 (Early Bird 15%, Combo Sekolah, Grosir BUMN).
   - Halaman Kontak & Lokasi Workshop Candi lengkap dengan fasilitas (Akses Tol, Parkir Kargo, Lounge Sampel) & panduan DP 50%.

---

## 📁 Struktur Folder Project

```text
kalenderia.my.id/
├── app.py                      # Controller utama Flask, routing, & endpoint SQLite/HTMX
├── init_db.py                  # Script seeder & struktur SQLite database (kalenderia.db)
├── generate_real_png.py        # Generator gambar fisik PNG realistis berbasis PIL
├── run_windows.bat             # Batch launcher otomatis 1-klik untuk Windows
├── requirements.txt            # Dependensi Python project
├── .gitignore                  # Berkas pengecualian Git
├── README.md                   # Dokumentasi resmi repository
│
├── static/
│   ├── css/
│   │   ├── input.css           # Source directive Tailwind v4 & keyframes animasi
│   │   └── style.css           # Result kompilasi Tailwind CSS ter-minify (35 KB)
│   ├── images/
│   │   └── real/               # Folder gambar fisik PNG realistis (meja, dinding, poster, dll.)
│   ├── main.js                 # Active-state manager, drawer controller, & HTMX handler
│   ├── favicon.svg             # Favicon vektor inisial "K" presisi
│   ├── favicon.ico             # Favicon ICO 32x32 multi-resolution
│   ├── favicon-32x32.png       # PNG Icon 32x32
│   ├── favicon-16x16.png       # PNG Icon 16x16
│   └── apple-touch-icon.png    # Apple Touch Icon 180x180
│
└── templates/
    ├── layout.html             # Master layout HTML5, meta OpenGraph, top mobile header, & drawer
    ├── index.html              # Fallback template
    ├── *_page.html             # Full wrapper pages untuk direct page load tanpa HTMX
    └── partials/               # Komponen partial untuk swap dinamis HTMX
        ├── sidebar.html        # Navigasi sidebar dengan ikon SVG 20x20 locked
        ├── home_content.html   # Beranda utama, hero workshop, bento box, & produk populer
        ├── products.html       # Katalog produk cetak kalender 2027
        ├── product_detail.html # Detail produk, spesifikasi kertas, & kalkulator WA
        ├── templates_list.html # Galeri template ready cetak 2027
        ├── papers.html         # Spesifikasi jenis kertas & gramasi (Art Paper, Art Carton, HVS)
        ├── portfolio.html      # Portofolio & bukti cetak B2B instansi
        ├── promo.html          # Penawaran Promo Pre-Order 2027 (3 Tier B2B)
        ├── about.html          # Profil workshop & lokasi Candi Sidoarjo (Deep Slate solid)
        ├── contact.html        # Kontak WA fast response & jam operasional pabrik
        └── tracking.html       # Lacak status resi & progres produksi pesanan
```

---

## 📞 Informasi Kontak & Workshop

- **Nama Workshop**: Kalenderia Workshop Candi Sidoarjo
- **Alamat**: Jl. Raya Candi No. 88, Candi, Kabupaten Sidoarjo, Jawa Timur 61271
- **WhatsApp Fast Response**: [0857-0000-0000](https://wa.me/6285700000000)
- **Tahun Aktif Produksi**: 2027
