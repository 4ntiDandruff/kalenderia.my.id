@echo off
title Kalenderia.my.id - Windows Automated Launcher
echo ============================================================
echo      KALENDERIA.MY.ID - WINDOWS AUTOMATED LAUNCHER
echo ============================================================
echo.

:: 1. Cek ketersediaan Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan di sistem Anda!
    echo Silakan install Python dari https://www.python.org/
    echo PASTIKAN mencentang "Add python.exe to PATH" saat install.
    echo.
    pause
    exit /b 1
)

:: 2. Buat virtual environment jika belum ada
if not exist "venv" (
    echo [1/4] Membuat Virtual Environment Python (venv)...
    python -m venv venv
)

:: 3. Aktifkan virtual environment & install dependensi
echo [2/4] Mengaktifkan Virtual Environment ^& Memasang Dependensi...
call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet

:: 4. Inisialisasi Database & Render Gambar Fisik PNG
echo [3/4] Menginisialisasi Database SQLite ^& Render Gambar Fisik PNG...
python init_db.py
python generate_real_png.py

:: 5. Menjalankan Server Web Flask
echo [4/4] Menjalankan Server Aplikasi Web Kalenderia...
echo.
echo ============================================================
echo  Aplikasi Berhasil Dijalankan!
echo  Buka Browser Anda ^& Masuk Ke Alamat: http://localhost:5005
echo  (Tekan CTRL+C di jendela ini untuk menghentikan server)
echo ============================================================
echo.

python app.py
pause
