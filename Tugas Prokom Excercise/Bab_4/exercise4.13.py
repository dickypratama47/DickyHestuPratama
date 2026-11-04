menu = ('nasi goreng', 'ayam bakar', 'sate', 'soto', 'rendang')

print("Menu awal:")
for m in menu:
    print(m)

# Jika tanda pagar di bawah dihapus, program akan error 
# karena isi tuple tidak bisa diubah satu per satu (permanen).
# menu[0] = 'mie goreng' 

# Cara yang sah adalah membuat tuple baru 
# dan menimpanya ke variabel yang sama secara keseluruhan.
menu = ('mie goreng', 'ayam bakar', 'sate', 'bakso', 'rendang') 

print("\nMenu baru:")
for m in menu:
    print(m)