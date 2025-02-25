pp = float(input('peso dos peixes em quilos: '))
ex = (pp - 50)
multa = ex * 4

if pp < 50:
    multa = 0
    ex = 0

print(f'pesagem: {pp:.1f} KG')
print(f'o excesso de peso é: {ex:.1f} KG')
print(f'o valor da multa é: R$ {multa:.2f}')