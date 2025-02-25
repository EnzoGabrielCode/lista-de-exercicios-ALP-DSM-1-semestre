a = float(input('1º número: '))
b = float(input('2º número: '))
c = float(input('3º número: '))

if a > b and a > c:
    print(f'{a} é o maior!')
elif b > c and b > a:
    print(f'{b} é o maior!')
else:
    print(f'{c} é o maior!')

if a < b and a < c:
    print(f'{a} é o menor!')
elif b < a and b < c:
    print(f'{b} é o menor!')
else:
    print(f'{c} é o menor!')