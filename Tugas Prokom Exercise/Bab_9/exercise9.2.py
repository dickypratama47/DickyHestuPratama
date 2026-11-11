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

# Membuat tiga instance (objek) restoran yang berbeda
restaurant_1 = Restaurant('Ratatouille', 'Italia')
restaurant_2 = Restaurant('Sederhana', 'Padang')
restaurant_3 = Restaurant('Sushi Tei', 'Jepang')

# Memanggil metode describe_restaurant() untuk masing-masing restoran
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()