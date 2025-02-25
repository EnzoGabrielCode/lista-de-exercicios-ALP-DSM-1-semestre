a = input('1º número: ')
b = input('2º número: ')
c = input('3º número: ')

if a > b and a > c:
    print(f'{a} é o maior!')
elif b > c > a:
    print(f'{b} é o maior!')
else:
    print(f'{c} é o maior!')