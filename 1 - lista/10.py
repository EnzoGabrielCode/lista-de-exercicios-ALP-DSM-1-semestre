cigarros = int(input('quantos cigarros são fumados por dia: '))
anos = int(input('por quantos anos o usuário fuma: '))
calculo = (((cigarros * 10) * (anos * 365)) / 60) / 24

print(f'voce perdeu aproximadamente {calculo:.1f} dias de vida')