from random import choice

# 1. Menyiapkan daftar angka dan huruf sesuai pilihan Anda
lottery_pool = [3, 5, 7, 8, 9, 15, 25, 30, 47, 68, 'C', 'D', 'Y', 'N', 'S']

# 2. Menyiapkan wadah kosong untuk tiket pemenang
winning_ticket = []

print("Mengacak undian lotre...\n")

# 3. Mengambil 4 elemen secara acak dengan prosedur perulangan (while)
# Kita menggunakan loop untuk memastikan tidak ada elemen yang terambil dua kali
while len(winning_ticket) < 4:
    pulled_item = choice(lottery_pool)
    
    # Hanya menambahkan elemen ke tiket jika belum ada di dalamnya
    if pulled_item not in winning_ticket:
        print(f"Karakter ditarik: {pulled_item}")
        winning_ticket.append(pulled_item)

# 4. Menampilkan hasil akhir tiket pemenang
print(f"\nSelamat! Tiket apa pun yang memiliki kombinasi {winning_ticket} adalah pemenangnya.")