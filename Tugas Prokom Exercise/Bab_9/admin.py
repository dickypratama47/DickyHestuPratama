"""Sebuah modul khusus untuk hak istimewa dan kelas admin."""

# Mengimpor kelas dasar User dari modul user.py
from user import User

class Privileges:
    """Memodelkan hak istimewa yang hanya dimiliki oleh admin."""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nHak Istimewa Admin:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- Tidak ada hak istimewa khusus.")

class Admin(User):
    """Memodelkan admin, sebagai turunan dari kelas User."""
    def __init__(self, first_name, last_name, location, major, privileges):
        super().__init__(first_name, last_name, location, major)
        self.privileges = Privileges(privileges)