class Restaurant:
    """Memodelkan sebuah restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan informasi restoran."""
        print(f"Restoran {self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang sudah buka!")

# 1. Membuat instance (objek) dari kelas Restaurant
restaurant = Restaurant('Ratatouille', 'Italia')

# 2. Mencetak kedua atribut secara individual
print(f"Nama restoran: {restaurant.restaurant_name}")
print(f"Jenis masakan: {restaurant.cuisine_type}")

# 3. Memanggil kedua metode
print("\n--- Deskripsi dan Status ---")
restaurant.describe_restaurant()
restaurant.open_restaurant()