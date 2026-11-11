# Mengimpor kelas Admin dari modul admin.py
from admin import Admin

# Menyiapkan daftar hak istimewa
hak_istimewa = [
    "bisa menambah pengguna", 
    "bisa menghapus komentar", 
    "bisa memblokir akun", 
    "bisa melihat statistik server"
]

# Membuat objek dari kelas Admin
admin_1 = Admin('Dicky', 'Pratama', 'Jakarta', 'Matematika', hak_istimewa)

# Menguji program
admin_1.describe_user()
admin_1.privileges.show_privileges()