import random

numeros = random.sample(range(1, 101), 20)
pares = []
impares = []
i = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
    i = i + 1

print(f'esses são os números: {numeros}')
print(f'esses são pares:      {pares}')
print(f'esses são impares:    {impares}')
