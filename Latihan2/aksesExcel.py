import openpyxl as pyxl
# Path, Nama file, dan sheet

FILE_NAME = "files/Nilai_KelasA.xlsx"
wb = pyxl.load_workbook(FILE_NAME, data_only=True)
sheet = wb["Nilai_A"]

# Membaca dan menampilkan hasil
for row in sheet.iter_rows(min_row=1, max_row=36, min_col=1, max_col=7):
    print([cell.value for cell in row])