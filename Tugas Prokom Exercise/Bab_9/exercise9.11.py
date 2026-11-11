# Mengimpor kelas Admin (yang otomatis membawa kelas User dan Privileges) dari modul user.py
from user import Admin

# Menyiapkan daftar hak istimewa
hak_istimewa = [
    "bisa menambah pengguna", 
    "bisa menghapus komentar", 
    "bisa memblokir akun", 
    "bisa melihat statistik server"
]

# Membuat objek dari kelas Admin
admin_1 = Admin('Dicky', 'Pratama', 'Jakarta', 'Matematika', hak_istimewa)

# Memanggil metode untuk memastikan modul bekerja dengan baik
admin_1.describe_user()
admin_1.privileges.show_privileges()