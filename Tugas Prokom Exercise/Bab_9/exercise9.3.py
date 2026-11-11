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

# Membuat beberapa instance (objek) pengguna
user_1 = User('dicky', 'pratama', 'surakarta', 'teknik industri')
user_2 = User('budi', 'santoso', 'jakarta', 'ilmu komputer')
user_3 = User('ada', 'lovelace', 'london', 'matematika')

# Memanggil kedua metode untuk masing-masing pengguna
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()