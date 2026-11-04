guests = ['Neymar', 'Ronaldo', 'Salah', 'Messi', 'Mbappe', 'Kane', 'Hakimi']

print("Maaf, meja makannya ternyata sudah penuh. Saya hanya bisa mengundang dua orang.\n")

batal1 = guests.pop()
print(f"Maaf {batal1}, saya tidak bisa mengundang Anda.")

batal2 = guests.pop()
print(f"Maaf {batal2}, saya tidak bisa mengundang Anda.")

batal3 = guests.pop()
print(f"Maaf {batal3}, saya tidak bisa mengundang Anda.")

batal4 = guests.pop(2)
print(f"Maaf {batal4}, saya tidak bisa mengundang Anda.")

batal5 = guests.pop(0)
print(f"Maaf {batal5}, saya tidak bisa mengundang Anda.\n")

print(f"Halo {guests[0]}, Anda masih tetap diundang!")
print(f"Halo {guests[1]}, Anda masih tetap diundang!\n")

del guests[0]
del guests[0]

print(guests)