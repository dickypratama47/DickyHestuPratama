pizzas = ['Pepperoni', 'Meat Lovers', 'Margherita']
pizzas_teman = pizzas[:] 

pizzas.append('Hawaiian')
pizzas_teman.append('Mushroom')

print("Pizza favorit saya adalah:")
for p in pizzas:
    print(p)

print("\nPizza favorit teman saya adalah:")
for t in pizzas_teman:
    print(t)