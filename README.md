# 📅 Kalenderia.my.id — Website Workshop Percetakan Kalender 2027 (Sidoarjo)

**Kalenderia.my.id** adalah platform katalog interaktif & penawaran B2B percetakan kalender presisi berbasis di Workshop Candi, Sidoarjo (Tahun Aktif Produksi: **2027**). Dibangun dengan arsitektur **Clean Light Workshop**, menggabungkan kecepatan **Python Flask**, keindahan **Tailwind CSS v4 Standalone**, interaktivitas seamless **HTMX**, serta gambar mockup fisik realistis resolusi tinggi hasil render Pillow (PIL).

---

## 💻 PANDUAN LENGKAP UNTUK PENGGUNA WINDOWS (AWAM / PEMULA)

Bagi Anda yang menggunakan komputer/laptop sistem operasi Windows dan ingin menjalankan aplikasi ini di laptop sendiri tanpa pengalaman coding, ikuti langkah-langkah praktis berikut secara berurutan:

---

### 📥 Langkah 1: Download & Install Python di Windows

1. Buka browser (Google Chrome / Edge) dan kunjungi situs resmi Python: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Klik tombol **"Download Python 3.12"** (atau versi 3.10 ke atas).
3. Buka file installer `.exe` yang sudah di-download.
4. ⚠️ **SANGAT PENTING**: Sebelum mengklik "Install Now", **Centang/Checklist** opsi **"Add python.exe to PATH"** di bagian paling bawah installer!
5. Klik **"Install Now"** lalu tunggu hingga muncul tulisan *Setup was successful*, kemudian klik **Close**.

---

### 💻 Langkah 2: Download Project dari GitHub

**Pilihan A (Tanpa Git - Paling Mudah):**
1. Masuk ke halaman utama repositori ini di browser.
2. Klik tombol hijau **`Code`** di kanan atas.
3. Pilih **`Download ZIP`**.
4. Setelah ter-download, **Extract** file `.zip` tersebut ke folder yang mudah diakses, contohnya di `C:\kalenderia.my.id`.

**Pilihan B (Menggunakan Git):**
Buka **Command Prompt (CMD)** atau **PowerShell**, lalu ketik:
```cmd
git clone https://github.com/4ntiDandruff/kalenderia.my.id.git
cd kalenderia.my.id
```

---

### ⚡ Langkah 3: Menjalankan Aplikasi di Windows (Metode Otomatis 1-Klik)

Untuk kemudahan pengguna Windows, project ini menyediakan script jalankan otomatis:

1. Buka folder tempat Anda meng-extract project (misalnya folder `kalenderia.my.id`).
2. Cari file bernama **`run_windows.bat`**.
3. **Klik 2x (Double-click)** pada file `run_windows.bat` tersebut.
4. Script akan otomatis:
   - Membuat Virtual Environment Python (`venv`)
   - Memasang seluruh dependensi pustaka yang dibutuhkan (`Flask`, `Pillow`, dll.)
   - Membuat file database lokal (`kalenderia.db`)
   - Meng-generate seluruh gambar sampel kalender fisik (`static/images/real/`)
   - Menjalankan server aplikasi web di komputer Anda!
5. Buka Google Chrome/Edge dan ketik alamat: **`http://localhost:5005`** atau **`http://127.0.0.1:5005`**.

---

### 🛠️ Langkah 4: Menjalankan Manual via Command Prompt (CMD) di Windows

Jika Anda lebih memilih menjalankan perintah satu per satu lewat CMD Windows:

1. Tekan tombol `Windows + R` di keyboard, ketik **`cmd`**, lalu tekan **Enter**.
2. Masuk ke folder project dengan mengetik:
   ```cmd
   cd C:\kalenderia.my.id
   ```
   *(Sesuaikan path folder dengan lokasi tempat Anda menyimpan project)*

3. Buat Virtual Environment Python:
   ```cmd
   python -m venv venv
   ```

4. Aktifkan Virtual Environment di Windows:
   ```cmd
   venv\Scripts\activate.bat
   ```
   *(Akan muncul tanda `(venv)` di sebelah kiri Command Prompt)*

5. Install seluruh dependensi pustaka:
   ```cmd
   pip install -r requirements.txt
   ```

6. Inisialisasi Database & Generate Gambar Sampel:
   ```cmd
   python init_db.py
   python generate_real_png.py
   ```

7. Jalankan Server Web:
   ```cmd
   python app.py
   ```

8. Buka browser favorit Anda di alamat: **`http://localhost:5005`**.

---

### ❓ Troubleshooting FAQ (Kendala Umum di Windows)

* **T: Muncul pesan error `'python' is not recognized as an internal or external command`**
  * **Solusi**: Anda belum mencentang opsi *"Add python.exe to PATH"* saat install Python. Uninstall Python Anda, lalu install ulang dan pastikan centang opsi tersebut di bagian bawah layar pertama installer.

* **T: Muncul error PowerShell Execution Policy saat aktivasi `venv`**
  * **Solusi**: Gunakan **Command Prompt (CMD)** biasa, bukan PowerShell. Atau jalankan file **`run_windows.bat`** langsung.

* **T: Bagaimana cara menghentikan server aplikasi?**
  * **Solusi**: Di jendela CMD yang sedang berjalan, tekan tombol **`Ctrl + C`** di keyboard.

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
