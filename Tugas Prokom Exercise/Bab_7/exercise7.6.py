aktif = True

while aktif:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    
    if topping == 'quit':
        aktif = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.\n")