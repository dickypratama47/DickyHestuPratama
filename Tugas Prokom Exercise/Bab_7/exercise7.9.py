sandwich_orders = ['tuna', 'pastrami', 'ayam', 'pastrami', 'keju', 'pastrami', 'daging']
finished_sandwiches = []

print("Maaf, hari ini kami kehabisan pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")