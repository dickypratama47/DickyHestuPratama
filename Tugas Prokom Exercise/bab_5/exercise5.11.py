# Latihan 5-11: Ordinal Numbers

# Membuat list angka 1 sampai 9
angka = list(range(1, 10))

for a in angka:
    if a == 1:
        print("1st")
    elif a == 2:
        print("2nd")
    elif a == 3:
        print("3rd")
    else:
        print(f"{a}th")