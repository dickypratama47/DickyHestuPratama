import csv
FILE_NAME = 'files/nilaiKuliah.csv'
listNilai = []
with open(FILE_NAME) as csvfile: # Buka file
    # Melakukan parsing untuk pembacaan seluruh baris
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    # Melakukan penyimpanan baris-baris data menjadi nested list
    for baris in readCSV:
        if line_count == 0:
            print(f'Nama Kolom : {baris}')
            line_count += 1
        else:
            print(baris)
            listNilai.append(baris)
            line_count += 1
    print(f'Total {line_count} baris')

csvfile.close() # Tutup file
print("isi nested list yang dibuat :")
print(listNilai)