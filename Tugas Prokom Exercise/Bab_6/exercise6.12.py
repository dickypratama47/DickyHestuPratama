people = {
    'dicky': {
        'full_name': 'dicky hestu pratama',
        'location': 'surakarta',
        'hobbies': ['catur', 'menonton film', 'mendengarkan musik']
    },
    'budi': {
        'full_name': 'budi santoso',
        'location': 'jakarta',
        'hobbies': ['membaca', 'bersepeda']
    }
}

for username, info in people.items():
    print(f"\nUsername: {username}")
    print(f"Nama Lengkap: {info['full_name'].title()}")
    print(f"Lokasi: {info['location'].title()}")
    print("Hobi:")
    for hobi in info['hobbies']:
        print(f"- {hobi.title()}")