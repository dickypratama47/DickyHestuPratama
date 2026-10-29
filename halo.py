def FtoC(f):
    c=(f-32)*5/9
    return c
f1=float(input(f'Masukkan suhu fahrenheit:'))
print(f1)
hasil=FtoC(f1)
print('Suhu dalam celcius:', hasil, 'C')