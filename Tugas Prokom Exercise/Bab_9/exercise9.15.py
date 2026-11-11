from random import choice

def get_winning_ticket(pool):
    """Fungsi pembantu untuk menarik 4 elemen acak dari wadah undian."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(pool)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """
    Memeriksa apakah seluruh elemen di tiket kita 
    terdapat di dalam tiket pemenang (urutan tidak masalah).
    """
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True


# 1. Menyiapkan daftar undian dan tiket kita
lottery_pool = [3, 5, 7, 8, 9, 15, 25, 30, 47, 68, 'C', 'D', 'Y', 'N', 'S']
my_ticket = [68, 8, 'N', 'S']

# 2. Menyiapkan variabel penghitung dan status kemenangan
plays = 0
won = False
max_tries = 1_000_000 # Batas aman agar program tidak berjalan selamanya

print("Memulai simulasi penarikan lotre. Ini mungkin memakan waktu sejenak...")

# 3. Memulai perulangan sampai tiket kita menang
while not won:
    new_winning_ticket = get_winning_ticket(lottery_pool)
    plays += 1
    won = check_ticket(my_ticket, new_winning_ticket)
    
    # Menghentikan program jika sudah mencoba 1 juta kali tanpa hasil
    if plays >= max_tries:
        break

# 4. Menampilkan hasil analisis
if won:
    print(f"\nTiket kita     : {my_ticket}")
    print(f"Tiket pemenang : {new_winning_ticket}")
    print(f"Luar biasa! Kita harus mengacak sebanyak {plays} kali sampai menang.")
else:
    print(f"\nMenyerah setelah {plays} kali percobaan tanpa kemenangan.")