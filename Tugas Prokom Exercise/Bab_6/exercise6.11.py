cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': 522364,
        'fact': 'dikenal sebagai pusat kebudayaan jawa'
    },
    'tokyo': {
        'country': 'jepang',
        'population': 13929286,
        'fact': 'kota metropolitan terbesar di dunia'
    },
    'paris': {
        'country': 'prancis',
        'population': 2161000,
        'fact': 'terkenal dengan menara eiffel'
    }
}

for kota, info in cities.items():
    print(f"\nKota: {kota.title()}")
    print(f"Negara: {info['country'].title()}")
    print(f"Populasi: {info['population']}")
    print(f"Fakta: {info['fact'].capitalize()}.")