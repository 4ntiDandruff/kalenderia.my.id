# 📅 Kalenderia.my.id — Website Workshop Percetakan Kalender 2027 (Sidoarjo)

**Kalenderia.my.id** adalah platform katalog interaktif & penawaran B2B percetakan kalender presisi berbasis di Workshop Candi, Sidoarjo (Tahun Aktif Produksi: **2027**). Dibangun dengan arsitektur **Clean Light Workshop**, menggabungkan kecepatan **Python Flask**, keindahan **Tailwind CSS v4 Standalone**, interaktivitas seamless **HTMX**, serta gambar mockup fisik realistis resolusi tinggi hasil render Pillow (PIL).

---

## 🛠️ Tech Stack & Ekosistem

- **Backend Framework**: Python 3.10+ / Flask (dengan helper interseptor `is_hx_request()`)
- **Database Layer**: SQLite 3 (`kalenderia.db`) disemai via `init_db.py`
- **Frontend Engine**: Jinja2 Templates + HTMX v1.9.10 (Single-Page Experience partial swap)
- **UI Design System**: Tailwind CSS v4 Standalone (Clean Light Workshop & Emerald Palette `#10b981`)
- **Asset Mockup Generator**: Python Pillow (PIL) `generate_real_png.py` untuk gambar fisik PNG realistis
- **Process Manager**: PM2 / Gunicorn (`http://127.0.0.1:5005`)

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

## ⚙️ Cara Menjalankan Project (Local Development)

### 1. Clone Repository & Buat Virtual Environment
```bash
git clone https://github.com/hizamnahari/kalenderia.my.id.git
cd kalenderia.my.id
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependensi Python
```bash
pip install -r requirements.txt
```

### 3. Inisialisasi Database & Generate Aset Gambar
```bash
python3 init_db.py
python3 generate_real_png.py
```

### 4. Kompilasi Tailwind CSS (Jika Mengubah input.css atau Template)
```bash
# Menggunakan Standalone Tailwind CSS CLI v4
/tmp/tailwindcss -i static/css/input.css -o static/css/style.css --content "templates/**/*.html" --minify
```

### 5. Jalankan Application Server
```bash
python3 app.py
```
Akses di browser pada alamat `http://127.0.0.1:5005` atau `http://localhost:5005`.

---

## 📞 Informasi Kontak & Workshop

- **Nama Workshop**: Kalenderia Workshop Candi Sidoarjo
- **Alamat**: Jl. Raya Candi No. 88, Candi, Kabupaten Sidoarjo, Jawa Timur 61271
- **WhatsApp Fast Response**: [0857-0000-0000](https://wa.me/6285700000000)
- **Tahun Aktif Produksi**: 2027
