import os
import sqlite3

def init_database():
    db_path = os.path.join(os.path.dirname(__file__), 'kalenderia.db')
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # 1. Table Categories
    c.execute('''
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            description TEXT,
            icon TEXT,
            image_url TEXT
        )
    ''')

    # 2. Table Products
    c.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            description TEXT,
            category_id INTEGER,
            min_order INTEGER DEFAULT 100,
            price_start INTEGER,
            wholesale_price TEXT,
            size TEXT,
            paper_type TEXT,
            finishing TEXT,
            image_url TEXT,
            is_featured INTEGER DEFAULT 0,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')

    # 3. Table Templates
    c.execute('''
        CREATE TABLE templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            theme_tag TEXT NOT NULL,
            formats TEXT NOT NULL,
            image_url TEXT NOT NULL,
            is_popular INTEGER DEFAULT 0
        )
    ''')

    # 4. Table Kertas / Materials
    c.execute('''
        CREATE TABLE materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gsm TEXT NOT NULL,
            description TEXT,
            best_for TEXT,
            image_url TEXT
        )
    ''')

    # 5. Table Portfolio
    c.execute('''
        CREATE TABLE portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            project_title TEXT NOT NULL,
            category TEXT NOT NULL,
            qty INTEGER NOT NULL,
            year INTEGER NOT NULL,
            location TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
    ''')

    # SEED DATA CATEGORIES
    c.executemany('''
        INSERT INTO categories (id, name, slug, description, icon, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Kalender Meja', 'kalender-meja', 'Kalender meja eksklusif untuk kantor, instansi, & souvenir perusahaan', '📅', '/static/images/real/kalender_meja.png'),
        (2, 'Kalender Dinding', 'kalender-dinding', 'Kalender gantung klem seng & spiral wire-o untuk sekolah & komunitas', '🖼️', '/static/images/real/kalender_dinding.png'),
        (3, 'Kalender Khusus', 'kalender-khusus', 'Kalender poster A3+, magnet kulkas, & bentuk kustom unik', '✨', '/static/images/real/kalender_poster.png')
    ])

    # SEED DATA PRODUCTS
    c.executemany('''
        INSERT INTO products (id, name, slug, description, category_id, min_order, price_start, wholesale_price, size, paper_type, finishing, image_url, is_featured)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Kalender Meja Standar A5 (13 Lembar)', 'kalender-meja-standar-a5', 
         'Kalender meja landscape/portrait ukuran A5 (15x21 cm), isi 7/13 lembar Art Paper 210g, tatakan karton tebal board 40, jilid spiral wire-o.',
         1, 50, 14500, 'Rp 14.500 - 22.000', 'A5 (15 x 21 cm)', 'Art Paper 210 gsm', 'Spiral Wire-O + Hardcover Board', '/static/images/real/kalender_meja.png', 1),
        
        (2, 'Kalender Meja Hardcover Premium Foil Gold', 'kalender-meja-hardcover-premium',
         'Kalender meja mewah dengan cetak poli emas/perak logo perusahaan pada tatakan hardcover linen/kraft tebal.',
         1, 50, 18500, 'Rp 18.500 - 28.000', 'A5 / B6 Custom', 'Art Carton 230 gsm', 'Hotprint Foil Gold + Wire-O', '/static/images/real/kalender_meja.png', 1),

        (3, 'Kalender Dinding Klem Seng (4 Lembar)', 'kalender-dinding-klem-seng-4-lembar',
         'Kalender dinding 4 lembar (3 bulanan), isi Art Paper 150g, jilid klem seng merah presisi dengan mata ayam gantungan.',
         2, 100, 7500, 'Rp 7.500 - 12.000', '38 x 53 cm (Standar)', 'Art Paper 150 gsm', 'Klem Seng Merah + Lubang Gantungan', '/static/images/real/kalender_dinding.png', 1),

        (4, 'Kalender Dinding Klem Seng (6 Lembar)', 'kalender-dinding-klem-seng-6-lembar',
         'Kalender dinding 6 lembar (2 bulanan), cetak warna tajam full color, cocok untuk promosi toko & sekolah.',
         2, 100, 9500, 'Rp 9.500 - 15.000', '38 x 53 cm (Standar)', 'Art Paper 150 gsm', 'Klem Seng Presisi', '/static/images/real/kalender_dinding.png', 0),

        (5, 'Kalender Dinding Islami & Waktu Sholat', 'kalender-dinding-islami',
         'Kalender dinding khusus lengkap dengan jadwal sholat 5 waktu Sidoarjo/Surabaya, tanggalan Hijriyah, & pasaran Jawa.',
         2, 100, 8000, 'Rp 8.000 - 13.500', '38 x 53 cm / 44 x 64 cm', 'Art Paper 150 gsm / HVS 80g', 'Klem Seng / Spiral Wire-O', '/static/images/real/kalender_islami.png', 1),

        (6, 'Kalender Poster A3+ (1 Lembar)', 'kalender-poster-a3',
         'Kalender poster tunggal 1 lembar tahunan full year 2027, bahan Art Carton 260g tebal mengkilap.',
         3, 100, 3500, 'Rp 3.500 - 6.500', 'A3+ (32 x 48 cm)', 'Art Carton 260 gsm', 'Cetak Full Color + Mata Ayam', '/static/images/real/kalender_poster.png', 0),

        (7, 'Kalender Magnet Kulkas Souvenir', 'kalender-magnet-kulkas',
         'Kalender mini souvenir unik berlapis magnet kulkas kaku, cocok untuk merchandise pernikahan & branding.',
         3, 200, 4500, 'Rp 4.500 - 8.000', '10 x 15 cm Custom', 'Art Carton + Rubber Magnet', 'Cut to Shape + Pad 12 Lembar', '/static/images/real/kalender_magnet.png', 0)
    ])

    # SEED DATA TEMPLATES
    c.executemany('''
        INSERT INTO templates (id, title, category, theme_tag, formats, image_url, is_popular)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Template Corporate Elegant BUMN 2027', 'Kalender Meja', 'Tema Corporate & BUMN', 'CDR, AI, PSD, PDF', '/static/images/real/kalender_meja.png', 1),
        (2, 'Template Masjid & Ornamen Islami 1448 H', 'Kalender Dinding', 'Tema Islami & Masjid', 'CDR, PSD, PDF', '/static/images/real/kalender_islami.png', 1),
        (3, 'Template Yayasan & Sekolah Modern', 'Kalender Dinding', 'Tema Sekolah & Education', 'CDR, AI, PDF', '/static/images/real/kalender_dinding.png', 1),
        (4, 'Template Instansi Pemerintah & Dinas', 'Kalender Meja', 'Tema Instansi & Komunitas', 'CDR, PSD, PDF', '/static/images/real/kalender_meja.png', 0),
        (5, 'Template Minimalist Clean Studio', 'Kalender Poster', 'Tema Corporate & BUMN', 'AI, PSD, PDF', '/static/images/real/kalender_poster.png', 0),
        (6, 'Template Pesantren & Lembaga Al-Qur\'an', 'Kalender Dinding', 'Tema Islami & Masjid', 'CDR, PDF', '/static/images/real/kalender_islami.png', 0)
    ])

    # SEED DATA MATERIALS
    c.executemany('''
        INSERT INTO materials (id, name, gsm, description, best_for, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Art Paper', '150 gsm', 'Kertas licin halus mengkilap, hasil cetak tajam, standar kalender dinding klem seng.', 'Kalender Dinding 4/6/12 Lembar', '/static/images/real/kalender_dinding.png'),
        (2, 'Art Paper Premium', '210 gsm', 'Kertas tebal premium dengan daya serap tinta tinggi, lentur dan tidak gampang melengkung.', 'Kalender Meja Standar A5', '/static/images/real/kalender_meja.png'),
        (3, 'Art Carton', '260 gsm / 310 gsm', 'Karton tebal kaku, sangat cocok untuk isi kalender meja eksklusif & poster A3+.', 'Kalender Meja Premium & Poster', '/static/images/real/kalender_poster.png'),
        (4, 'HVS Premium', '80 gsm / 100 gsm', 'Kertas putih doff mudah ditulis bulpen/spidol, cocok untuk kalender kerja/catatan.', 'Kalender Kerja & Kantor', '/static/images/real/kalender_dinding.png')
    ])

    # SEED DATA PORTFOLIO
    c.executemany('''
        INSERT INTO portfolio (id, client_name, project_title, category, qty, year, location, image_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'RSUD Krian Sidoarjo', 'Kalender Meja Eksklusif Dokter & Manajemen', 'Kalender Meja', 1200, 2026, 'Sidoarjo', '/static/images/real/kalender_meja.png'),
        (2, 'Dinas Pendidikan Kab. Sidoarjo', 'Kalender Dinding Sekolah & SD-SMP', 'Kalender Dinding', 5000, 2026, 'Sidoarjo', '/static/images/real/kalender_dinding.png'),
        (3, 'PT Maspion Group', 'Kalender Meja Hardcover Corporate', 'Kalender Meja', 3500, 2026, 'Surabaya', '/static/images/real/kalender_meja.png'),
        (4, 'KSP Bina Artha Mandiri', 'Kalender Dinding Klem Seng 4 Lembar', 'Kalender Dinding', 2500, 2026, 'Sidoarjo', '/static/images/real/kalender_dinding.png'),
        (5, 'Yayasan Al-Hikmah Surabaya', 'Kalender Dinding Islami & Jadwal Sholat', 'Kalender Dinding', 4000, 2026, 'Surabaya', '/static/images/real/kalender_islami.png'),
        (6, 'Komunitas Alumni Unair', 'Kalender Poster Custom Souvenir', 'Kalender Poster', 1500, 2026, 'Surabaya', '/static/images/real/kalender_poster.png')
    ])

    conn.commit()
    conn.close()
    print("Database SQLite kalenderia.db berhasil di-inisialisasi ulang dengan gambar PNG fisik lengkap!")

if __name__ == '__main__':
    init_database()
