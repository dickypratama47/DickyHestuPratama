sandwich_orders = ['tuna', 'ayam', 'keju', 'daging']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")