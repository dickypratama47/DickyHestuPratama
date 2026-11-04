angka_favorit = {
    'dicky': [47, 30, 8],
    'andi': [9, 11],
    'siti': [12, 14, 20],
    'rudi': [3],
    'joko': [10, 88]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()}:")
    for a in angka:
        print(f"- {a}")