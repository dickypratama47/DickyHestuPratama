class Car:
    """Memodelkan mobil secara umum."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """Memodelkan baterai untuk mobil listrik (Komposisi)."""

    def __init__(self, battery_size=40):
        """Inisialisasi atribut baterai, default 40 kWh."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Menampilkan informasi kapasitas baterai."""
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        """Menampilkan perkiraan jarak tempuh berdasarkan kapasitas baterai."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"Mobil ini dapat menempuh jarak sekitar {range} mil saat daya penuh.")

    # --- Metode Baru untuk Latihan 9.9 ---
    def upgrade_battery(self):
        """Memeriksa dan memperbarui kapasitas baterai jika belum maksimal."""
        if self.battery_size != 65:
            print("Melakukan proses upgrade baterai...")
            self.battery_size = 65
        else:
            print("Baterai sudah memiliki kapasitas maksimal (65-kWh).")


class ElectricCar(Car):
    """Memodelkan aspek khusus dari mobil listrik."""

    def __init__(self, make, model, year):
        """
        Inisialisasi atribut dari kelas induk.
        Lalu inisialisasi atribut baterai sebagai sebuah objek tersendiri.
        """
        super().__init__(make, model, year)
        # Menjadikan objek Battery sebagai atribut (Komposisi)
        self.battery = Battery()


# 1. Membuat objek mobil listrik (akan menggunakan baterai default 40 kWh)
my_ev = ElectricCar('nissan', 'leaf', 2024)
print(f"Mobil baru saya: {my_ev.get_descriptive_name()}")

# 2. Mengecek kapasitas baterai dan jarak tempuh awal
my_ev.battery.describe_battery()
my_ev.battery.get_range()

# 3. Melakukan upgrade baterai
print("\n--- Membawa mobil ke bengkel ---")
my_ev.battery.upgrade_battery()

# 4. Mengecek kembali kapasitas baterai dan jarak tempuh setelah di-upgrade
print("\n--- Setelah Upgrade ---")
my_ev.battery.describe_battery()
my_ev.battery.get_range()