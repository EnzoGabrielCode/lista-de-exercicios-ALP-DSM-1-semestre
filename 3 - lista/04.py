n = int(input('digite um número inteiro: '))
a, b = 1, 1

if n <= 0:
    print("Número inválido")
elif n == 1:
    print([0])
else:
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
    print(b)
