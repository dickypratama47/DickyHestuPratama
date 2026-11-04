favorite_places = {
    'dicky': ['bali', 'jakarta'],
    'budi': ['bandung', 'yogyakarta', 'surabaya'],
    'siti': ['lombok']
}

for nama, tempat in favorite_places.items():
    print(f"\nTempat favorit {nama.title()}:")
    for t in tempat:
        print(f"- {t.title()}")