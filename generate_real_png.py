import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('/home/michael/kalenderia.my.id/static/images/real', exist_ok=True)

font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font_path_reg = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

font_title = ImageFont.truetype(font_path, 22)
font_sub = ImageFont.truetype(font_path_reg, 14)
font_date = ImageFont.truetype(font_path, 11)
font_day = ImageFont.truetype(font_path, 10)

def draw_real_kalender_meja():
    img = Image.new('RGB', (600, 400), color='#1E293B')
    d = ImageDraw.Draw(img)
    d.ellipse([100, 340, 500, 380], fill='#0F172A')
    d.polygon([(120, 350), (160, 80), (440, 80), (480, 350)], fill='#0F172A', outline='#334155', width=3)
    d.polygon([(120, 350), (480, 350), (460, 365), (140, 365)], fill='#020617')
    d.rectangle([140, 60, 460, 330], fill='#FFFFFF', outline='#CBD5E1', width=2)
    d.rectangle([140, 60, 460, 130], fill='#059669')
    d.text((160, 75), "KALENDER MEJA 2027", font=font_title, fill='#FFFFFF')
    d.text((160, 105), "PT. MEGAPASS INTRA SOLUSINDO", font=font_sub, fill='#A7F3D0')
    d.rectangle([340, 145, 445, 250], fill='#ECFDF5', outline='#10B981', width=2)
    d.text((355, 190), "[ FOTO ]\n [ LOGO ]", font=font_day, fill='#047857', align="center")
    d.text((160, 145), "JANUARI 2027", font=ImageFont.truetype(font_path, 14), fill='#0F172A')
    
    days = ["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"]
    for i, day in enumerate(days):
        color = '#DC2626' if i == 0 else '#475569'
        d.text((160 + (i * 24), 170), day, font=font_day, fill=color)

    dates = [
        ["", "", "", "", "", "1", "2"],
        ["3", "4", "5", "6", "7", "8", "9"],
        ["10", "11", "12", "13", "14", "15", "16"],
        ["17", "18", "19", "20", "21", "22", "23"],
        ["24", "25", "26", "27", "28", "29", "30"],
        ["31", "", "", "", "", "", ""]
    ]
    for r, row in enumerate(dates):
        for c, val in enumerate(row):
            if val:
                color = '#DC2626' if c == 0 else '#1E293B'
                d.text((160 + (c * 24), 188 + (r * 18)), val, font=font_date, fill=color)

    for x in range(155, 450, 20):
        d.ellipse([x, 54, x+8, 66], fill='#0F172A')
        d.arc([x-2, 40, x+10, 64], start=180, end=360, fill='#94A3B8', width=4)
        d.arc([x-2, 40, x+10, 64], start=180, end=360, fill='#E2E8F0', width=2)

    img.save('/home/michael/kalenderia.my.id/static/images/real/kalender_meja.png')

def draw_real_kalender_dinding():
    img = Image.new('RGB', (600, 400), color='#0F172A')
    d = ImageDraw.Draw(img)
    d.line([(300, 10), (220, 40)], fill='#E2E8F0', width=2)
    d.line([(300, 10), (380, 40)], fill='#E2E8F0', width=2)
    d.ellipse([295, 5, 305, 15], fill='#94A3B8')
    d.rectangle([180, 40, 420, 380], fill='#FFFFFF', outline='#CBD5E1', width=2)
    d.rectangle([170, 35, 430, 52], fill='#B91C1C', outline='#7F1D1D', width=2)
    d.ellipse([296, 40, 304, 48], fill='#FFFFFF')
    d.rectangle([195, 65, 405, 190], fill='#047857')
    d.text((215, 115), "KALENDER DINDING 2027", font=font_title, fill='#FFFFFF')
    d.text((215, 145), "CETAK 4 LEMBAR / 12 LEMBAR", font=font_sub, fill='#A7F3D0')
    d.rectangle([195, 205, 405, 360], fill='#F8FAFC', outline='#E2E8F0', width=1)
    d.rectangle([200, 210, 400, 230], fill='#059669')
    d.text((210, 214), "WAKTU SHOLAT & PASARAN JAWA", font=font_day, fill='#FFFFFF')

    days = ["MIN", "SEN", "SEL", "RAB", "KAM", "JUM", "SAB"]
    for i, day in enumerate(days):
        color = '#DC2626' if i == 0 else '#334155'
        d.text((205 + (i * 28), 240), day, font=font_day, fill=color)

    for r in range(4):
        for c in range(7):
            num = str(r * 7 + c + 1)
            color = '#DC2626' if c == 0 else '#0F172A'
            d.text((205 + (c * 28), 260 + (r * 22)), num, font=font_date, fill=color)

    img.save('/home/michael/kalenderia.my.id/static/images/real/kalender_dinding.png')

def draw_real_kalender_poster():
    img = Image.new('RGB', (600, 400), color='#1E1B4B')
    d = ImageDraw.Draw(img)
    d.rectangle([180, 20, 420, 380], fill='#FFFFFF', outline='#94A3B8', width=2)
    d.ellipse([295, 28, 305, 38], fill='#64748B', outline='#334155', width=2)
    d.rectangle([195, 45, 405, 120], fill='#0284C7')
    d.text((210, 65), "KALENDER POSTER 2027", font=font_title, fill='#FFFFFF')
    d.text((210, 95), "ART CARTON 260G FULL COLOR", font=font_sub, fill='#BAE6FD')

    for row in range(4):
        for col in range(3):
            x = 200 + (col * 70)
            y = 135 + (row * 58)
            d.rectangle([x, y, x + 60, y + 50], fill='#F0F9FF', outline='#BAE6FD', width=1)
            d.rectangle([x, y, x + 60, y + 14], fill='#0284C7')
            d.text((x + 5, y + 2), f"BULAN {row*3+col+1}", font=ImageFont.truetype(font_path, 8), fill='#FFFFFF')

    img.save('/home/michael/kalenderia.my.id/static/images/real/kalender_poster.png')

def draw_real_kalender_islami():
    img = Image.new('RGB', (600, 400), color='#064E3B')
    d = ImageDraw.Draw(img)
    d.line([(300, 10), (220, 40)], fill='#A7F3D0', width=2)
    d.line([(300, 10), (380, 40)], fill='#A7F3D0', width=2)
    d.ellipse([295, 5, 305, 15], fill='#34D399')
    d.rectangle([180, 40, 420, 380], fill='#FFFFFF', outline='#A7F3D0', width=2)
    d.rectangle([170, 35, 430, 52], fill='#047857', outline='#064E3B', width=2)
    d.ellipse([296, 40, 304, 48], fill='#FFFFFF')
    d.rectangle([195, 65, 405, 190], fill='#065F46')
    d.text((205, 105), "KALENDER ISLAMI 1448 H", font=font_title, fill='#FEF3C7')
    d.text((215, 140), "JADWAL SHOLAT & HIJRIYAH 2027", font=font_sub, fill='#A7F3D0')
    d.rectangle([195, 205, 405, 360], fill='#ECFDF5', outline='#A7F3D0', width=1)
    d.rectangle([200, 210, 400, 230], fill='#047857')
    d.text((215, 214), "SIDOARJO & SURABAYA MUKIM", font=font_day, fill='#FFFFFF')

    days = ["MIN", "SEN", "SEL", "RAB", "KAM", "JUM", "SAB"]
    for i, day in enumerate(days):
        color = '#DC2626' if i == 0 else '#065F46'
        d.text((205 + (i * 28), 240), day, font=font_day, fill=color)

    for r in range(4):
        for c in range(7):
            num = str(r * 7 + c + 1)
            color = '#DC2626' if c == 0 else '#064E3B'
            d.text((205 + (c * 28), 260 + (r * 22)), num, font=font_date, fill=color)

    img.save('/home/michael/kalenderia.my.id/static/images/real/kalender_islami.png')

def draw_real_kalender_magnet():
    img = Image.new('RGB', (600, 400), color='#475569')
    d = ImageDraw.Draw(img)
    # Kulkas Door Surface
    d.rectangle([150, 40, 450, 360], fill='#F1F5F9', outline='#94A3B8', width=3)
    # Magnet Souvenir Card
    d.rectangle([210, 100, 390, 300], fill='#FFFFFF', outline='#0284C7', width=3)
    d.rectangle([210, 100, 390, 160], fill='#0284C7')
    d.text((220, 115), "SOUVENIR MAGNET", font=font_sub, fill='#FFFFFF')
    d.text((220, 135), "KALENDER KULKAS", font=font_day, fill='#BAE6FD')
    # Mini Calendar Pad
    d.rectangle([230, 175, 370, 280], fill='#F8FAFC', outline='#CBD5E1', width=1)
    d.text((245, 215), "12 LEMBAR MINI", font=font_sub, fill='#0F172A')

    img.save('/home/michael/kalenderia.my.id/static/images/real/kalender_magnet.png')

draw_real_kalender_meja()
draw_real_kalender_dinding()
draw_real_kalender_poster()
draw_real_kalender_islami()
draw_real_kalender_magnet()
print("All 5 real PNG calendar graphics generated successfully!")
