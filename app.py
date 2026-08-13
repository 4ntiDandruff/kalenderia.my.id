import sqlite3
from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('kalenderia.db')
    conn.row_factory = sqlite3.Row
    return conn

def is_hx_request():
    return request.headers.get('HX-Request') == 'true'

@app.context_processor
def inject_global_vars():
    return {
        'wa_number': '6285700000000',
        'wa_display': '0857-0000-0000',
        'wa_link': 'https://wa.me/6285700000000?text=Halo%20Kalenderia,%20saya%20mau%20tanya%20cetak%20kalender%202027',
        'current_year': 2027
    }

# 1. BERANDA WORKSHOP ('/') - LANDING PAGE UTUH
@app.route('/')
def home():
    conn = get_db_connection()
    featured_products = conn.execute('SELECT * FROM products WHERE is_featured = 1 LIMIT 3').fetchall()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    
    template = 'home.html' if not is_hx_request() else 'partials/home_content.html'
    return render_template(template, 
                           products=featured_products, 
                           categories=categories, 
                           active_page='home',
                           title='Kalenderia - Workshop Percetakan Kalender Presisi Sidoarjo')

# 2. KATALOG PRODUK CETAK ('/katalog' & '/produk')
@app.route('/katalog')
@app.route('/produk')
def products():
    category_slug = request.args.get('kategori')
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    
    if category_slug:
        cat = conn.execute('SELECT id FROM categories WHERE slug = ?', (category_slug,)).fetchone()
        if cat:
            products_list = conn.execute('SELECT * FROM products WHERE category_id = ?', (cat['id'],)).fetchall()
        else:
            products_list = []
    else:
        products_list = conn.execute('SELECT * FROM products').fetchall()
        
    conn.close()
    
    template = 'products_page.html' if not is_hx_request() else 'partials/products.html'
    return render_template(template, 
                           products=products_list, 
                           categories=categories, 
                           selected_category=category_slug,
                           active_page='products',
                           title='Katalog Produk Cetak Kalender 2027 - Sidoarjo')

# 3. KATEGORI FILTER SPESIFIK ('/kategori/<slug>')
@app.route('/kategori/<slug>')
def category_detail(slug):
    conn = get_db_connection()
    category = conn.execute('SELECT * FROM categories WHERE slug = ?', (slug,)).fetchone()
    if not category:
        conn.close()
        abort(404)
        
    products_list = conn.execute('SELECT * FROM products WHERE category_id = ?', (category['id'],)).fetchall()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    
    template = 'products_page.html' if not is_hx_request() else 'partials/products.html'
    return render_template(template, 
                           products=products_list, 
                           categories=categories, 
                           category=category,
                           selected_category=slug,
                           active_page='products',
                           title=f"Katalog {category['name']} 2027 - Kalenderia")

# 4. DETAIL PRODUK ('/produk/<slug>')
@app.route('/produk/<slug>')
def product_detail(slug):
    conn = get_db_connection()
    product = conn.execute('SELECT p.*, c.name as category_name FROM products p JOIN categories c ON p.category_id = c.id WHERE p.slug = ?', (slug,)).fetchone()
    if not product:
        conn.close()
        abort(404)
        
    related = conn.execute('SELECT * FROM products WHERE category_id = ? AND id != ? LIMIT 3', (product['category_id'], product['id'])).fetchall()
    conn.close()
    
    template = 'product_detail_page.html' if not is_hx_request() else 'partials/product_detail.html'
    return render_template(template, 
                           product=product, 
                           related=related,
                           active_page='products',
                           title=f"{product['name']} - Kalenderia Sidoarjo")

# 5. TEMPLATE READY CETAK ('/template-desain')
@app.route('/template-desain')
def templates_page():
    theme_filter = request.args.get('tema')
    conn = get_db_connection()
    if theme_filter:
        design_templates = conn.execute('SELECT * FROM templates WHERE theme_tag = ?', (theme_filter,)).fetchall()
    else:
        design_templates = conn.execute('SELECT * FROM templates').fetchall()
    conn.close()
    
    template = 'templates_page.html' if not is_hx_request() else 'partials/templates_list.html'
    return render_template(template, 
                           templates=design_templates, 
                           selected_theme=theme_filter,
                           active_page='templates',
                           title='Galeri Template Ready Cetak Kalender 2027 - Free Custom Logo')

# 6. JENIS KERTAS & FINISHING ('/kertas')
@app.route('/kertas')
def papers_page():
    conn = get_db_connection()
    materials_list = conn.execute('SELECT * FROM materials').fetchall()
    conn.close()
    
    template = 'papers_page.html' if not is_hx_request() else 'partials/papers.html'
    return render_template(template, 
                           materials=materials_list,
                           active_page='papers',
                           title='Spesifikasi Jenis Kertas & Finishing Cetak - Kalenderia')

# 7. PROMO & PRE-ORDER 2027 ('/promo')
@app.route('/promo')
def promo_page():
    conn = get_db_connection()
    promo_products = conn.execute('SELECT * FROM products WHERE is_featured = 1').fetchall()
    conn.close()
    
    template = 'promo_page.html' if not is_hx_request() else 'partials/promo.html'
    return render_template(template, 
                           products=promo_products,
                           active_page='promo',
                           title='Promo Pre-Order Kalender 2027 Diskon Awal Tahun')

# 8. PORTOFOLIO HASIL CETAK ('/portofolio')
@app.route('/portofolio')
def portfolio_page():
    conn = get_db_connection()
    portfolio_list = conn.execute('SELECT * FROM portfolio').fetchall()
    conn.close()
    
    template = 'portfolio_page.html' if not is_hx_request() else 'partials/portfolio.html'
    return render_template(template, 
                           portfolio=portfolio_list,
                           active_page='portfolio',
                           title='Portofolio & Bukti Hasil Cetak - Workshop Kalenderia Sidoarjo')

# 9. PROFIL WORKSHOP CANDI ('/tentang-kami')
@app.route('/tentang-kami')
def about_page():
    template = 'about_page.html' if not is_hx_request() else 'partials/about.html'
    return render_template(template, 
                           active_page='about',
                           title='Profil Workshop & Profil Cetak Offset - Kalenderia Sidoarjo')

# 10. KONTAK & LOKASI ('/kontak')
@app.route('/kontak')
def contact_page():
    template = 'contact_page.html' if not is_hx_request() else 'partials/contact.html'
    return render_template(template, 
                           active_page='contact',
                           title='Kontak & Alamat Workshop Candi Sidoarjo - Kalenderia')

# 11. LACAK RESI PESANAN ('/cek-resi')
@app.route('/cek-resi', methods=['GET', 'POST'])
def tracking_page():
    result = None
    searched = False
    resi_query = request.args.get('resi', '').strip() or (request.form.get('resi', '').strip() if request.method == 'POST' else '')
    
    if resi_query:
        searched = True
        conn = get_db_connection()
        result = conn.execute('SELECT * FROM tracking WHERE UPPER(resi_code) = UPPER(?)', (resi_query,)).fetchone()
        conn.close()
        
    template = 'tracking_page.html' if not is_hx_request() else 'partials/tracking.html'
    return render_template(template, 
                           result=result, 
                           searched=searched, 
                           resi=resi_query,
                           active_page='tracking',
                           title='Lacak Status Resi & Produksi Pesanan - Kalenderia Sidoarjo')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
