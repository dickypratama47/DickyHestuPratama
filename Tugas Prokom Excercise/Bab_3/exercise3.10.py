mountains = ['Rinjani', 'Bromo', 'Merbabu', 'Semeru', 'Prau']
print(mountains)

print(mountains[0])

mountains.append('Slamet')
print(mountains)

mountains.insert(0, 'Kerinci')
print(mountains)

del mountains[1]
print(mountains)

mountains.pop()
print(mountains)

mountains.remove('Merbabu')
print(mountains)

print(sorted(mountains))

mountains.reverse()
print(mountains)

mountains.sort()
print(mountains)

mountains.sort(reverse=True)
print(mountains)

print(len(mountains))