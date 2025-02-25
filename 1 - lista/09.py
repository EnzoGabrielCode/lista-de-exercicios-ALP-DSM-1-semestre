kmPercorrido = float(input('quantos KMs foram percorridos: '))
dias = float(input('quantos dias o usuário ficou com o carro: '))
calculo = (60 * dias) + (kmPercorrido * 0.15)

print(f'o preço a ser pago é: {calculo}')