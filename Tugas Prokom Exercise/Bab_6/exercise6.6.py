favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

daftar_responden = ['jen', 'dicky', 'phil', 'budi', 'siti', 'edward']

for orang in daftar_responden:
    if orang in favorite_languages.keys():
        print(f"Terima kasih {orang.title()} telah mengikuti survei!")
    else:
        print(f"Halo {orang.title()}, silakan luangkan waktu untuk mengikuti survei.")