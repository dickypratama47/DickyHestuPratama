# 1. Modifikasi Latihan 4-1: Pizza
# Menggunakan list dan for loop dengan indentasi 4 spasi.

pizza_favorit = ['pepperoni', 'meat lovers', 'margherita']

for pizza in pizza_favorit:
    print(f"Saya sangat suka pizza {pizza}.")

print("\nSaya benar-benar menyukai pizza!")


# 2. Modifikasi Latihan 4-8: Cubes
# Membuat daftar pangkat tiga dari 1 sampai 10 menggunakan list comprehension 
# agar struktur kode tetap ringkas dan rapi.

kubik = [nilai**3 for nilai in range(1, 11)]

for angka in kubik:
    print(angka)


# 3. Modifikasi Latihan 4-13: Buffet
# Menggunakan tuple untuk menu restoran, dipisahkan dengan baris kosong 
# dari perintah pencetakan agar visualnya tidak bertumpuk.

menu_restoran = ('nasi goreng', 'ayam bakar', 'sate', 'capcay', 'es teh')

print("\nMenu awal restoran:")
for menu in menu_restoran:
    print(menu)