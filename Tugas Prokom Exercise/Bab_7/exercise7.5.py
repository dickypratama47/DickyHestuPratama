while True:
    umur = input("Masukkan umur Anda (ketik 'quit' untuk berhenti): ")
    
    if umur == 'quit':
        break
        
    umur = int(umur)
    if umur < 3:
        print("Tiket Anda gratis.\n")
    elif umur <= 12:
        print("Harga tiket Anda adalah $10.\n")
    else:
        print("Harga tiket Anda adalah $15.\n")