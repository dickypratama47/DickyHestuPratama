class Restaurant:
    """Memodelkan sebuah restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan informasi restoran."""
        print(f"Restoran {self.restaurant_name} menyajikan {self.cuisine_type}.")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang sudah buka!")


# --- Kelas Anak (Child Class) ---
class IceCreamStand(Restaurant):
    """Memodelkan kedai es krim, sebagai turunan dari Restaurant."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Inisialisasi atribut dari kelas induk (Restaurant).
        Kemudian inisialisasi atribut khusus untuk kedai es krim.
        """
        # super() memanggil metode __init__() dari kelas Restaurant
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print(f"\n{self.restaurant_name} memiliki varian rasa berikut:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# 1. Menyiapkan daftar rasa
rasa_tersedia = ['Cookies&Cream', 'Coklat', 'Vanilla', 'Stroberi', 'Matcha']

# 2. Membuat objek dari IceCreamStand
kedai_turki = IceCreamStand('Es Krim Turki', 'Es Krim & Dessert', rasa_tersedia)

# 3. Memanggil metode dari kelas induk (Restaurant)
kedai_turki.describe_restaurant()

# 4. Memanggil metode dari kelas anak (IceCreamStand)
kedai_turki.show_flavors()