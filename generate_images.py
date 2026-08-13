import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('/home/michael/kalenderia.my.id/static/images', exist_ok=True)

def draw_svg_meja_standar(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc"/>
          <stop offset="100%" stop-color="#e2e8f0"/>
        </linearGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#bg)"/>
      <g transform="translate(100, 30)">
        <path d="M 40 310 L 80 80 L 320 80 L 360 310 Z" fill="#0f172a" />
        <rect x="70" y="40" width="260" height="230" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="3"/>
        <rect x="90" y="60" width="130" height="24" rx="4" fill="#059669"/>
        <rect x="90" y="95" width="220" height="10" rx="2" fill="#0f172a"/>
        <rect x="90" y="115" width="220" height="8" rx="2" fill="#94a3b8"/>
        <rect x="90" y="130" width="220" height="8" rx="2" fill="#cbd5e1"/>
        <rect x="90" y="145" width="220" height="8" rx="2" fill="#e2e8f0"/>
        <rect x="90" y="160" width="220" height="8" rx="2" fill="#94a3b8"/>
        <rect x="90" y="175" width="220" height="8" rx="2" fill="#cbd5e1"/>
        <rect x="90" y="190" width="220" height="8" rx="2" fill="#e2e8f0"/>
        <rect x="90" y="210" width="150" height="12" rx="3" fill="#059669"/>
        <text x="95" y="77" font-family="sans-serif" font-weight="bold" font-size="12" fill="#ffffff">MEJA A5 SPIRAL</text>
        <circle cx="100" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
        <circle cx="140" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
        <circle cx="180" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
        <circle cx="220" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
        <circle cx="260" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
        <circle cx="300" cy="40" r="6" fill="#64748b" stroke="#1e293b" stroke-width="2"/>
      </g>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_dinding_islami(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#ecfdf5"/>
      <g transform="translate(170, 20)">
        <rect x="20" y="20" width="220" height="320" rx="4" fill="#ffffff" stroke="#a7f3d0" stroke-width="4"/>
        <rect x="10" y="10" width="240" height="18" rx="3" fill="#dc2626"/>
        <path d="M120 10 Q 130 0 140 10" stroke="#991b1b" stroke-width="3" fill="none"/>
        <rect x="35" y="40" width="190" height="110" rx="4" fill="#047857"/>
        <path d="M130 60 Q 110 90 130 120 Q 150 90 130 60" fill="#fef3c7"/>
        <text x="130" y="135" font-family="sans-serif" font-weight="bold" font-size="11" fill="#ffffff" text-anchor="middle">JADWAL SHOLAT &amp; HIJRIYAH</text>
        <rect x="35" y="165" width="190" height="150" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
        <rect x="45" y="180" width="170" height="12" rx="2" fill="#059669"/>
        <rect x="45" y="200" width="170" height="100" rx="2" fill="#e2e8f0"/>
      </g>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_magnet(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#f1f5f9"/>
      <g transform="translate(180, 50)">
        <rect x="0" y="0" width="240" height="300" rx="16" fill="#334155"/>
        <rect x="15" y="15" width="210" height="140" rx="10" fill="#059669"/>
        <text x="120" y="85" font-family="sans-serif" font-weight="extrabold" font-size="16" fill="#ffffff" text-anchor="middle">MAGNET KULKAS</text>
        <rect x="15" y="170" width="210" height="115" rx="8" fill="#ffffff"/>
        <rect x="30" y="185" width="180" height="85" fill="#e2e8f0"/>
      </g>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_template_corp(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a"/>
      <rect x="40" y="40" width="520" height="320" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
      <rect x="70" y="70" width="200" height="260" rx="8" fill="#0284c7"/>
      <text x="170" y="200" font-family="sans-serif" font-weight="black" font-size="20" fill="#ffffff" text-anchor="middle">CORPORATE BUMN</text>
      <rect x="290" y="70" width="240" height="260" rx="8" fill="#ffffff"/>
      <rect x="310" y="90" width="200" height="30" fill="#0284c7"/>
      <rect x="310" y="130" width="200" height="180" fill="#f1f5f9"/>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_template_sekolah(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#fff7ed"/>
      <rect x="40" y="40" width="520" height="320" rx="12" fill="#ffffff" stroke="#ffedd5" stroke-width="4"/>
      <rect x="70" y="70" width="460" height="100" rx="8" fill="#ea580c"/>
      <text x="300" y="130" font-family="sans-serif" font-weight="black" font-size="22" fill="#ffffff" text-anchor="middle">KALENDER SEKOLAH &amp; YAYASAN</text>
      <rect x="70" y="190" width="140" height="140" rx="6" fill="#fed7aa"/>
      <rect x="230" y="190" width="140" height="140" rx="6" fill="#fed7aa"/>
      <rect x="390" y="190" width="140" height="140" rx="6" fill="#fed7aa"/>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_template_instansi(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#f0fdf4"/>
      <rect x="40" y="40" width="520" height="320" rx="12" fill="#ffffff" stroke="#bbf7d0" stroke-width="3"/>
      <rect x="70" y="70" width="460" height="140" rx="8" fill="#16a34a"/>
      <text x="300" y="150" font-family="sans-serif" font-weight="black" font-size="24" fill="#ffffff" text-anchor="middle">INSTANSI &amp; KOMUNITAS</text>
      <rect x="70" y="225" width="460" height="100" rx="6" fill="#dcfce7"/>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_paper_artpaper(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#f8fafc"/>
      <rect x="100" y="50" width="400" height="300" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="3"/>
      <text x="300" y="200" font-family="sans-serif" font-weight="black" font-size="24" fill="#0f172a" text-anchor="middle">ART PAPER 120 / 150 GSM</text>
      <text x="300" y="230" font-family="sans-serif" font-size="14" fill="#059669" text-anchor="middle">Glossy, Halus, Tajam untuk Cetak Offset</text>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_paper_artcarton(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#f1f5f9"/>
      <rect x="100" y="50" width="400" height="300" rx="8" fill="#ffffff" stroke="#059669" stroke-width="4"/>
      <text x="300" y="200" font-family="sans-serif" font-weight="black" font-size="24" fill="#0f172a" text-anchor="middle">ART CARTON 210 / 260 GSM</text>
      <text x="300" y="230" font-family="sans-serif" font-size="14" fill="#059669" text-anchor="middle">Tebal, Kaku, Kokoh untuk Kalender Meja</text>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_paper_fancy(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#fafaf9"/>
      <rect x="100" y="50" width="400" height="300" rx="8" fill="#1c1917" stroke="#d97706" stroke-width="4"/>
      <text x="300" y="200" font-family="sans-serif" font-weight="black" font-size="24" fill="#fbbf24" text-anchor="middle">FANCY PAPER &amp; LINEN</text>
      <text x="300" y="230" font-family="sans-serif" font-size="14" fill="#f59e0b" text-anchor="middle">Mewah, Tekstur Eksklusif + Foil Gold</text>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

def draw_svg_paper_hvs(path):
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#ffffff"/>
      <rect x="100" y="50" width="400" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
      <text x="300" y="200" font-family="sans-serif" font-weight="black" font-size="24" fill="#334155" text-anchor="middle">HVS 80 / 100 GSM</text>
      <text x="300" y="230" font-family="sans-serif" font-size="14" fill="#64748b" text-anchor="middle">Doff Berserat, Mudah Ditulis Catatan</text>
    </svg>'''
    with open(path, 'w') as f:
        f.write(svg)

draw_svg_meja_standar('/home/michael/kalenderia.my.id/static/images/prod_meja.svg')
draw_svg_dinding_islami('/home/michael/kalenderia.my.id/static/images/prod_islami.svg')
draw_svg_magnet('/home/michael/kalenderia.my.id/static/images/prod_magnet.svg')

draw_svg_template_corp('/home/michael/kalenderia.my.id/static/images/tpl_corp.svg')
draw_svg_template_sekolah('/home/michael/kalenderia.my.id/static/images/tpl_sekolah.svg')
draw_svg_template_instansi('/home/michael/kalenderia.my.id/static/images/tpl_instansi.svg')

draw_svg_paper_artpaper('/home/michael/kalenderia.my.id/static/images/paper_artpaper.svg')
draw_svg_paper_artcarton('/home/michael/kalenderia.my.id/static/images/paper_artcarton.svg')
draw_svg_paper_fancy('/home/michael/kalenderia.my.id/static/images/paper_fancy.svg')
draw_svg_paper_hvs('/home/michael/kalenderia.my.id/static/images/paper_hvs.svg')

print("10 File gambar SVG kustom lokal berhasil di-generate!")
