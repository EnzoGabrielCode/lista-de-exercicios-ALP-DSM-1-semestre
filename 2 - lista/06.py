gph = float(input('ganho por hora: '))
h = int(input('horas trabalhadas: '))
d = int(input('dias trabalhados por mês: '))
bruto = (gph * h) * d
ir = (bruto * 0.11)
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print(f'+ Sário bruto: R$ {bruto:.2f}')
print(f'- IR(11%): R$ {ir:.2f}')
print(f'- INSS(8%): R$ {inss:.2f}')
print(f'- Sindicato(5%): R$ {sindicato:.2f}')
print(f'= Salário líquido: R$ {liquido:.2f}')