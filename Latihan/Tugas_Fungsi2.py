# ==========================================
# BAGIAN B: PROGRAM STUDI KASUS TERAPAN
# ==========================================

# 1. Tarif Parkir Kendaraan di Bandara
def hitung_tarif_parkir_bandara(jenis_kendaraan, durasi_jam):
    # Asumsi: Mobil/Motor tarif flat jam pertama, lalu per jam berikutnya
    if jenis_kendaraan.lower() == 'motor':
        tarif_awal = 5000
        tarif_per_jam = 2000
    else:  # mobil
        tarif_awal = 10000
        tarif_per_jam = 5000
    
    if durasi_jam <= 1:
        total = tarif_awal
    else:
        total = tarif_awal + (durasi_jam - 1) * tarif_per_jam
    return total

# 2. Menghitung Penggajian Sederhana
def hitung_gaji(nama, golongan, jam_kerja):
    # Gaji pokok berdasarkan golongan
    if golongan == 1:
        gaji_pokok = 3000000
    elif golongan == 2:
        gaji_pokok = 4500000
    else:
        gaji_pokok = 6000000
    
    # Lembur jika jam kerja > 160 jam/bulan, Rp 25.000/jam
    lembur = 0
    if jam_kerja > 160:
        lembur = (jam_kerja - 160) * 25000
        
    total_gaji = gaji_pokok + lembur
    return nama, gaji_pokok, lembur, total_gaji

# 3. Menghitung BBI (Berat Badan Ideal) dan Status Berat Badan (Rumus Broca)
def hitung_bbi(tinggi_cm, jenis_kelamin):
    # Pria: (Tinggi - 100) - ((Tinggi - 100) * 10%)
    # Wanita: (Tinggi - 100) - ((Tinggi - 100) * 15%)
    if jenis_kelamin.lower() == 'pria':
        bbi = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.10)
    else:
        bbi = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.15)
    return bbi

# 4. Tarif Parkir Kendaraan di Stasiun
def hitung_tarif_parkir_stasiun(durasi_jam):
    # Contoh tarif progresif stasiun: Flat 2 jam pertama Rp 4.000, selanjutnya Rp 2.000/jam
    if durasi_jam <= 2:
        return 4000
    else:
        return 4000 + (durasi_jam - 2) * 2000

# 5. Menentukan Kebutuhan Cairan Pengganti bagi Dehidrasi (Metode Holiday-Segar)
def hitung_kebutuhan_cairan(berat_badan_kg):
    # 10 kg pertama: 100 cc/kg/hari
    # 10 kg kedua: 50 cc/kg/hari
    # Sisanya: 20 cc/kg/hari
    if berat_badan_kg <= 10:
        cairan = berat_badan_kg * 100
    elif berat_badan_kg <= 20:
        cairan = (10 * 100) + ((berat_badan_kg - 10) * 50)
    else:
        cairan = (10 * 100) + (10 * 50) + ((berat_badan_kg - 20) * 20)
    return cairan # dalam ml / cc per hari

# 6. Menentukan Tarif Tol Kendaraan Berdasarkan Golongan
def hitung_tarif_tol(golongan):
    tarif_dict = {
        1: 12500, # Sedan, Jip, Pick Up, Truk Kecil
        2: 18500, # Truk 2 sumbu
        3: 22000, # Truk 3 sumbu
        4: 29000, # Truk 4 sumbu
        5: 35000  # Truk 5 sumbu atau lebih
    }
    return tarif_dict.get(golongan, 0)


# --- CONTOH UJI COBA PEMANGGILAN FUNGSI BAGIAN B ---
if __name__ == "__main__":
    print("\n=== HASIL UJI BAGIAN B ===")
    print(f"1. Tarif Parkir Bandara (Mobil, 3 jam) = Rp {hitung_tarif_parkir_bandara('Mobil', 3):,}")
    
    nm, gpok, lemb, tgaj = hitung_gaji("Dicky", 2, 170)
    print(f"2. Gaji Karyawan ({nm}): Pokok=Rp {gpok:,}, Lembur=Rp {lemb:,}, Total=Rp {tgaj:,}")
    
    print(f"3. BBI Pria (Tinggi 170 cm) = {hitung_bbi(170, 'pria'):.1f} kg")
    print(f"4. Tarif Parkir Stasiun (5 jam) = Rp {hitung_tarif_parkir_stasiun(5):,}")
    print(f"5. Kebutuhan Cairan (BB 55 kg) = {hitung_kebutuhan_cairan(55):,} ml/hari")
    print(f"6. Tarif Tol Golongan 1 = Rp {hitung_tarif_tol(1):,}")