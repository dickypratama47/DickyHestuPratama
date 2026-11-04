glosarium = {
    'list': 'Kumpulan item dalam urutan tertentu.',
    'tuple': 'List yang tidak bisa diubah nilainya.',
    'if': 'Struktur untuk menguji kondisi tertentu.',
    'dictionary': 'Kumpulan pasangan key-value.',
    'boolean': 'Tipe data yang bernilai True atau False.',
    'string': 'Deretan karakter teks.',
    'float': 'Tipe data angka desimal.',
    'loop': 'Perulangan untuk mengeksekusi kode berulang kali.',
    'key': 'Kunci unik dalam dictionary.',
    'value': 'Nilai yang diasosiasikan dengan key.'
}

for kata, arti in glosarium.items():
    print(f"\n{kata.title()}: {arti}")