def make_sandwich(*items):
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

make_sandwich('keju', 'tomat')
make_sandwich('daging', 'selada', 'mayo')
make_sandwich('ayam', 'keju', 'mentimun', 'saus sambal')