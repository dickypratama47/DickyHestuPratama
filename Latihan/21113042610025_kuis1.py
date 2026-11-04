# kuis1.py
import modul_kuis1

def main():
    upah_perjam = int(input("Masukkan upah perjam (misal 20000): "))
    
    # Kita gunakan list (daftar) sederhana untuk nama-nama hari
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    list_jam = []
    list_upah = []
    
    print("\nMasukkan waktu selesai lembur (misal 18.15). Ketik 0 jika tidak lembur.")
    
    # Meminta input menggunakan perulangan untuk setiap hari
    for h in hari:
        waktu = input("Waktu selesai " + h + " : ")
        
        # Panggil fungsi dari file modul_kuis1
        jam = modul_kuis1.hitung_jam(waktu)
        upah = modul_kuis1.hitung_upah(jam, upah_perjam)
        
        # Simpan hasil hitungannya ke dalam list
        list_jam.append(jam)
        list_upah.append(upah)
        
    # Cetak hasil akhir
    print("\n----------------------------------")
    total_semua = 0
    
    # Perulangan untuk menge-print data yang sudah disimpan tadi
    for i in range(len(hari)):
        print(hari[i], ":", list_jam[i], "jam -> Rp", list_upah[i])
        total_semua = total_semua + list_upah[i]
        
    print("Total : Rp", total_semua)

if __name__ == "__main__":
    main()