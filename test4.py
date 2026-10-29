def hitung_statistik_nilai(listNilai):
    total = 0
    for nilai in listNilai:
        total = total + nilai
    rataan = total / len(listNilai)
    # rataan = sum(listNilai)/len(listNilai) # ALternatif cara
    variansi = sum((x-rataan)**2 for x in listNilai) / len(listNilai)
    stddev = variansi ** 0.5
    return total, rataan, stddev

nilai_kelasA = [78, 89, 88, 97]

totalNIlai, rataanNilai, stdevNilai = hitung_statistik_nilai(nilai_kelasA)
print("Total Nilai Kelas : ", totalNIlai)
print("Rata-rata Nilai Kelas : ", rataanNilai)
print("Standar Deviasi Nilai Kelas : ", stdevNilai)