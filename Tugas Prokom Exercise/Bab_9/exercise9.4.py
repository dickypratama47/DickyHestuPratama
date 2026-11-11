class Restaurant:
    """Memodelkan sebuah restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Menambahkan nilai default 0
        self.number_served = 0 

    def describe_restaurant(self):
        """Menampilkan informasi restoran."""
        print(f"Restoran {self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang sudah buka!")

    # --- Metode Baru untuk Latihan 9.4 ---
    def set_number_served(self, number):
        """Menetapkan jumlah pelanggan yang telah dilayani."""
        self.number_served = number

    def increment_number_served(self, additional_served):
        """Menambah jumlah pelanggan yang telah dilayani."""
        self.number_served += additional_served


# 1. Membuat instance dari kelas Restaurant
restaurant = Restaurant('Ratatouille', 'Italia')

# 2. Mencetak jumlah pelanggan awal (akan tampil 0 karena nilai default)
print(f"Jumlah pelanggan awal: {restaurant.number_served}")

# 3. Mengubah nilai atribut secara LANGSUNG
restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

# 4. Mengubah nilai atribut melalui METODE set_number_served()
restaurant.set_number_served(45)
print(f"Jumlah pelanggan setelah menggunakan set_number_served: {restaurant.number_served}")

# 5. Menambah nilai atribut melalui METODE increment_number_served()
restaurant.increment_number_served(20)
print(f"Jumlah pelanggan setelah ditambah 20 pelanggan baru: {restaurant.number_served}")