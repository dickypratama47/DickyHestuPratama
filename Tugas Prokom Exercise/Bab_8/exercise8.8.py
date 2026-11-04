def make_album(artist, title):
    return {'artist': artist.title(), 'title': title.title()}

while True:
    print("\nMasukkan informasi album (ketik 'quit' untuk berhenti):")
    artis_input = input("Nama artis: ")
    if artis_input == 'quit':
        break
    
    judul_input = input("Judul album: ")
    if judul_input == 'quit':
        break
    
    album_baru = make_album(artis_input, judul_input)
    print(album_baru)