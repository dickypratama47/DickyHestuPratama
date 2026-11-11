class User:
    """Memodelkan profil pengguna sederhana."""

    def __init__(self, first_name, last_name, location, major):
        """Inisialisasi profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.major = major

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\n--- Profil {self.first_name.title()} ---")
        print(f"Nama Lengkap : {self.first_name.title()} {self.last_name.title()}")
        print(f"Domisili     : {self.location.title()}")
        print(f"Bidang Studi : {self.major.title()}")

    def greet_user(self):
        """Menampilkan ucapan sapaan kepada pengguna."""
        print(f"Halo, {self.first_name.title()}! Semoga harimu menyenangkan.")


# --- Kelas Anak (Child Class) ---
class Admin(User):
    """Memodelkan admin, sebagai turunan dari kelas User."""

    def __init__(self, first_name, last_name, location, major, privileges):
        """
        Inisialisasi atribut dari kelas induk (User).
        Kemudian inisialisasi atribut khusus untuk admin.
        """
        super().__init__(first_name, last_name, location, major)
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak istimewa yang dimiliki admin."""
        print(f"\nHak Istimewa Admin {self.first_name.title()}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# 1. Menyiapkan daftar hak istimewa untuk admin
hak_istimewa_admin = [
    "bisa menambah pengguna", 
    "bisa menghapus komentar", 
    "bisa memblokir akun", 
    "bisa melihat statistik server"
]

# 2. Membuat objek dari kelas Admin
admin_1 = Admin('Dicky', 'Pratama', 'Jakarta', 'Matematika', hak_istimewa_admin)

# 3. Memanggil metode dari kelas induk
admin_1.describe_user()

# 4. Memanggil metode dari kelas anak
admin_1.show_privileges()