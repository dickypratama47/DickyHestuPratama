makanan_saya = ['pizza', 'falafel', 'kue wortel']
makanan_teman = makanan_saya[:]

makanan_saya.append('cannoli')
makanan_teman.append('es krim')

print("Makanan favorit saya adalah:")
for makanan in makanan_saya:
    print(makanan)

print("\nMakanan favorit teman saya adalah:")
for makanan in makanan_teman:
    print(makanan)