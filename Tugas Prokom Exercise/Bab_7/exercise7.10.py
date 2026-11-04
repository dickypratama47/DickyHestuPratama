responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    
    responses[name] = response
    
    repeat = input("Apakah Anda ingin membiarkan orang lain merespons? (ya/tidak) ")
    if repeat.lower() == 'tidak':
        polling_active = False

print("\n--- Hasil Polling ---")
for name, response in responses.items():
    print(f"{name.title()} ingin pergi ke {response.title()}.")