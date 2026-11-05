pet_1 = {'jenis': 'kucing', 'pemilik': 'dicky'}
pet_2 = {'jenis': 'anjing', 'pemilik': 'budi'}
pet_3 = {'jenis': 'burung', 'pemilik': 'siti'}

pets = [pet_1, pet_2, pet_3]

for p in pets:
    print(f"Hewan {p['jenis']} ini dimiliki oleh {p['pemilik'].title()}.")