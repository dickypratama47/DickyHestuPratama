orang_1 = {'first_name': 'budi', 'last_name': 'santoso', 'age': 20, 'city': 'surakarta'}
orang_2 = {'first_name': 'andi', 'last_name': 'wijaya', 'age': 22, 'city': 'jakarta'}
orang_3 = {'first_name': 'siti', 'last_name': 'aminah', 'age': 19, 'city': 'bandung'}

people = [orang_1, orang_2, orang_3]

for p in people:
    nama = f"{p['first_name'].title()} {p['last_name'].title()}"
    print(f"Nama: {nama}, Umur: {p['age']}, Kota: {p['city'].title()}")