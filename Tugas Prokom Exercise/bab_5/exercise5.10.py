# Latihan 5-10: Checking Usernames

current_users = ['admin', 'dicky', 'budi', 'siti', 'joko']
new_users = ['Dicky', 'SITI', 'ahmad', 'sarah', 'rudi']

# Membuat salinan daftar pengguna saat ini dengan huruf kecil semua 
# agar pengecekan tidak sensitif terhadap huruf besar/kecil (case-insensitive)
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username '{new_user}' sudah digunakan. Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")