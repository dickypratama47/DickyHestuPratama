# modul_kuis1.py

def hitung_jam(waktu):
    # Jika pengguna mengetik 0, berarti tidak lembur
    if waktu == "0":
        return 0
        
    # Memisahkan jam dan menit berdasarkan tanda titik (misal "18.15")
    pecahan = waktu.split(".")
    jam = int(pecahan[0])
    menit = int(pecahan[1])
    
    # Ubah semuanya ke dalam satuan menit agar mudah dikurangi
    waktu_selesai = (jam * 60) + menit
    waktu_mulai = (16 * 60) + 30      # Jam 16.30 diubah ke menit
    
    selisih = waktu_selesai - waktu_mulai
    
    # Jika selisihnya kurang dari 0 (pulang sebelum 16.30), jam lembur = 0
    if selisih <= 0:
        return 0
        
    # Hitung jam lembur pakai pembagian bulat (//)
    jam_lembur = selisih // 60
    
    # Batas maksimal yang dihitung adalah 4 jam
    if jam_lembur > 4:
        jam_lembur = 4
        
    return jam_lembur

def hitung_upah(jam_lembur, upah_perjam):
    total = 0
    
    # Tambahkan upah perlahan-lahan berdasarkan jumlah jam
    if jam_lembur >= 1:
        total = total + (1.5 * upah_perjam)
    if jam_lembur >= 2:
        total = total + (2.0 * upah_perjam)
    if jam_lembur >= 3:
        total = total + (2.0 * upah_perjam)
    if jam_lembur >= 4:
        total = total + (3.0 * upah_perjam)
        
    # Ubah hasil akhir ke integer agar tidak ada .0 di belakangnya
    return int(total)