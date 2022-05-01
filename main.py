lista = []
while True:
    beker = input('Szám: ')
    if beker == 'x' or beker == 'X':
        break
    else:
        lista.append(beker)

print(lista)
print(f'Legkisebb lista elem: {min(lista)}')
print(f'Legnagyobb lista elem: {max(lista)}')
