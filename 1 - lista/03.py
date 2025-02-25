dias = int(input("quantidade de dias: "))
horas = int(input("quantidade de horas: "))
minutos = int(input("quantidade de minutos: "))
segundos = int(input("quantidade de segundos: "))

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print (f'o total é: {total} segundos')