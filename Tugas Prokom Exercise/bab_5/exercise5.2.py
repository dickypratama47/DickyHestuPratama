# 1. Pengujian kesamaan dan ketidaksamaan string (== dan !=)
jurusan = 'Teknik Industri'
print("Apakah jurusan == 'Teknik Industri'? Saya tebak Benar.")
print(jurusan == 'Teknik Industri')

print("\nApakah jurusan != 'Teknik Mesin'? Saya tebak Benar.")
print(jurusan != 'Teknik Mesin')

# 2. Pengujian menggunakan fungsi lower()
nama = 'Dicky'
print("\nApakah nama.lower() == 'dicky'? Saya tebak Benar.")
print(nama.lower() == 'dicky')

# 3. Pengujian angka (==, !=, >, <, >=, <=)
nilai = 95
print("\nApakah nilai > 90? Saya tebak Benar.")
print(nilai > 90)

print("\nApakah nilai <= 90? Saya tebak Salah.")
print(nilai <= 90)

# 4. Pengujian menggunakan 'and' dan 'or'
semester = 3
print("\nApakah nilai > 90 and semester == 3? Saya tebak Benar.")
print(nilai > 90 and semester == 3) # Benar karena KEDUANYA terpenuhi

print("\nApakah nilai > 90 or semester == 5? Saya tebak Benar.")
print(nilai > 90 or semester == 5) # Benar karena SALAH SATU (nilai > 90) terpenuhi

# 5. Pengujian apakah suatu item ADA (in) atau TIDAK ADA (not in) di dalam list
lab_teknik = ['lpske', 'lstars', 'rsaki']
print("\nApakah 'lpske' in lab_teknik? Saya tebak Benar.")
print('lpske' in lab_teknik)

print("\nApakah 'lab bahasa' not in lab_teknik? Saya tebak Benar.")
print('lab bahasa' not in lab_teknik)