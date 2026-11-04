sungai = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'misisipi': 'amerika serikat'
}

for s, k in sungai.items():
    print(f"Sungai {s.title()} mengalir melewati negara {k.title()}.")

print("\nDaftar nama sungai:")
for s in sungai.keys():
    print(s.title())

print("\nDaftar nama negara:")
for k in sungai.values():
    print(k.title())