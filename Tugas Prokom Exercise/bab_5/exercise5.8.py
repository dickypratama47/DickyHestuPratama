# Latihan 5-8: Hello Admin

usernames = ['admin', 'dicky', 'budi', 'siti', 'joko']

for user in usernames:
    if user == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {user.title()}, terima kasih sudah login kembali.")