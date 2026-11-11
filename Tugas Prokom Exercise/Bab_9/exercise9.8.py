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


# --- Kelas Baru untuk Komposisi ---
class Privileges:
    """Memodelkan hak istimewa yang hanya dimiliki oleh admin."""

    def __init__(self, privileges=[]):
        """Inisialisasi atribut hak istimewa."""
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak istimewa."""
        print(f"\nHak Istimewa Admin:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- Tidak ada hak istimewa khusus.")


# --- Kelas Anak (Child Class) ---
class Admin(User):
    """Memodelkan admin, sebagai turunan dari kelas User."""

    def __init__(self, first_name, last_name, location, major, privileges):
        """
        Inisialisasi atribut dari kelas induk (User).
        Kemudian inisialisasi atribut privileges menggunakan kelas Privileges.
        """
        super().__init__(first_name, last_name, location, major)
        # Menjadikan instance dari kelas Privileges sebagai atribut
        self.privileges = Privileges(privileges)


# 1. Menyiapkan daftar hak istimewa
hak_istimewa_admin = [
    "bisa menambah pengguna", 
    "bisa menghapus komentar", 
    "bisa memblokir akun", 
    "bisa melihat statistik server"
]

# 2. Membuat objek dari kelas Admin
admin_1 = Admin('Dicky', 'Pratama', 'Jakarta', 'Matematika', hak_istimewa_admin)

# 3. Memanggil metode describe_user() dari kelas User
admin_1.describe_user()

# 4. Memanggil metode show_privileges() melalui atribut privileges
admin_1.privileges.show_privileges()