from random import randint

class Die:
    """Memodelkan dadu sederhana yang bisa dilempar."""

    def __init__(self, sides=6):
        """Inisialisasi atribut dadu, default 6 sisi."""
        self.sides = sides

    def roll_die(self):
        """Mengembalikan nilai acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sides)


# 1. Dadu 6 sisi (10 kali lemparan)
dadu_6 = Die(6)
hasil_6 = []
for _ in range(10):
    hasil_6.append(dadu_6.roll_die())
print(f"Hasil 10 kali lemparan dadu 6 sisi:\n{hasil_6}\n")

# 2. Dadu 10 sisi (10 kali lemparan)
dadu_10 = Die(10)
hasil_10 = []
for _ in range(10):
    hasil_10.append(dadu_10.roll_die())
print(f"Hasil 10 kali lemparan dadu 10 sisi:\n{hasil_10}\n")

# 3. Dadu 20 sisi (10 kali lemparan)
dadu_20 = Die(20)
hasil_20 = []
for _ in range(10):
    hasil_20.append(dadu_20.roll_die())
print(f"Hasil 10 kali lemparan dadu 20 sisi:\n{hasil_20}\n")

# 4. Dadu 100 sisi (10 kali lemparan)
dadu_100 = Die(100)
hasil_100 = []
for _ in range(10):
    hasil_100.append(dadu_100.roll_die())
print(f"Hasil 10 kali lemparan dadu 100 sisi:\n{hasil_100}")