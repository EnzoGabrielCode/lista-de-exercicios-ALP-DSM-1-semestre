habitantesA = 80000
habitantesB = 200000
i = 0

while True:
    print(f'o total de habitantes no {i}º na cidade A é: {habitantesA:.0f}')
    print(f'o total de habitantes no {i}º na cidade B é: {habitantesB:.0f}')
    print('-----------------------------------------------------------')

    if habitantesA >= habitantesB:
        break
    else:
        habitantesA = habitantesA + (habitantesA * 0.03)
        habitantesB = habitantesB + (habitantesB * 0.015)
        i = i + 1

print(f'foram precisos {i} anos')