# ==========================================
# BAGIAN A: PROGRAM KONVERSI SUHU & GEOMETRI
# ==========================================

import math

# 1. Konversi Fahrenheit ke Celcius
def fahrenheit_ke_celcius(f):
    return (f - 32) * 5 / 9

# 2. Konversi Celcius ke Fahrenheit
def celcius_ke_fahrenheit(c):
    return (c * 9 / 5) + 32

# 3. Konversi Fahrenheit ke Reamur
def fahrenheit_ke_reamur(f):
    return (f - 32) * 4 / 9

# 4. Konversi Reamur ke Fahrenheit
def reamur_ke_fahrenheit(r):
    return (r * 9 / 4) + 32

# 5. Konversi Celcius ke Reamur
def celcius_ke_reamur(c):
    return c * 4 / 5

# 6. Konversi Reamur ke Celcius
def reamur_ke_celcius(r):
    return r * 5 / 4

# 7. Luas Lingkaran
def luas_lingkaran(r):
    return math.pi * (r ** 2)

# 8. Luas Permukaan Tabung (2 * pi * r * (r + t))
def luas_permukaan_tabung(r, t):
    return 2 * math.pi * r * (r + t)

# 9. Volume Tabung (pi * r^2 * t)
def volume_tabung(r, t):
    return math.pi * (r ** 2) * t


# --- CONTOH UJI COBA PEMANGGILAN FUNGSI BAGIAN A ---
if __name__ == "__main__":
    print("=== HASIL UJI BAGIAN A ===")
    print(f"1. 212°F ke Celcius = {fahrenheit_ke_celcius(212):.2f} °C")
    print(f"2. 100°C ke Fahrenheit = {celcius_ke_fahrenheit(100):.2f} °F")
    print(f"3. 212°F ke Reamur = {fahrenheit_ke_reamur(212):.2f} °R")
    print(f"4. 80°R ke Fahrenheit = {reamur_ke_fahrenheit(80):.2f} °F")
    print(f"5. 100°C ke Reamur = {celcius_ke_reamur(100):.2f} °R")
    print(f"6. 80°R ke Celcius = {reamur_ke_celcius(80):.2f} °C")
    print(f"7. Luas Lingkaran (r=7) = {luas_lingkaran(7):.2f}")
    print(f"8. Luas Permukaan Tabung (r=7, t=10) = {luas_permukaan_tabung(7, 10):.2f}")
    print(f"9. Volume Tabung (r=7, t=10) = {volume_tabung(7, 10):.2f}")