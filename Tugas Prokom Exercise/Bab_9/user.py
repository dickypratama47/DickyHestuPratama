"""Sebuah modul untuk merepresentasikan pengguna secara umum."""

class User:
    """Memodelkan profil pengguna sederhana."""
    def __init__(self, first_name, last_name, location, major):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.major = major

    def describe_user(self):
        print(f"\n--- Profil {self.first_name.title()} ---")
        print(f"Nama Lengkap : {self.first_name.title()} {self.last_name.title()}")
        print(f"Domisili     : {self.location.title()}")
        print(f"Bidang Studi : {self.major.title()}")