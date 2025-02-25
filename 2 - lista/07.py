a = float(input('área em metros quadrados a ser pintada: '))
litrosNecessarios = a / 3
latasNecessarias = (litrosNecessarios // 18) + 1
total = latasNecessarias * 80

print(f'você precisará de {latasNecessarias} latas')
print(f'o total a se pagar é R$ {total:.2f}')