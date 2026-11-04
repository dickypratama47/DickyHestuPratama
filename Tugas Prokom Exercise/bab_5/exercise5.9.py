# Latihan 5-9: No Users

usernames = []  # List sengaja dikosongkan untuk menguji logika

if usernames:  # Blok ini akan bernilai False jika list kosong
    for user in usernames:
        if user == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {user.title()}, terima kasih sudah login kembali.")
else:
    print("Kita perlu menemukan beberapa pengguna!")