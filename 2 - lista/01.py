a = int(input('1º lado: '))
b = int(input('2º lado: '))
c = int(input('3º lado: '))

if a == b and b == c and a == c:
    print('o triângulo é equilátero!')
elif a == b or a == c or b == c:
    print('o triângulo é isóceles!')
else:
    print('o trângulo é escaleno!')