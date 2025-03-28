import random

vetor1 = random.sample(range(1, 101), 10)
vetor2 = random.sample(range(1, 101), 10)
vetor3 = []
i = 0

while True:
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    i = i + 1
    if len(vetor3) == 20:
        break

print(vetor1)
print(vetor2)
print(vetor3)