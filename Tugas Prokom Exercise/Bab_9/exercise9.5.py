class User:
    """Memodelkan profil pengguna sederhana."""

    def __init__(self, first_name, last_name, location, major):
        """Inisialisasi profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.major = major
        # Atribut baru dengan nilai default 0
        self.login_attempts = 0

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\n--- Profil {self.first_name.title()} ---")
        print(f"Nama Lengkap : {self.first_name.title()} {self.last_name.title()}")
        print(f"Domisili     : {self.location.title()}")
        print(f"Bidang Studi : {self.major.title()}")

    def greet_user(self):
        """Menampilkan ucapan sapaan kepada pengguna."""
        print(f"Halo, {self.first_name.title()}! Semoga harimu menyenangkan.")

    # --- Metode Baru untuk Latihan 9.5 ---
    def increment_login_attempts(self):
        """Menambah nilai percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang nilai percobaan login menjadi 0."""
        self.login_attempts = 0


# 1. Membuat instance (objek) pengguna
user_1 = User('dicky', 'pratama', 'surakarta', 'teknik industri')

# 2. Mensimulasikan percobaan login beberapa kali
print("Mencoba login...")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Mencetak jumlah percobaan login
print(f"Jumlah percobaan login saat ini: {user_1.login_attempts}")

# 3. Mereset jumlah percobaan login
print("\nMereset percobaan login...")
user_1.reset_login_attempts()

# Mencetak kembali jumlah percobaan login untuk memastikan sudah menjadi 0
print(f"Jumlah percobaan login setelah direset: {user_1.login_attempts}")