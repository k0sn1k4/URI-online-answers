tipo = input()
matriz = []; linha = []
for i in range(0, 12):
    for n in range(0, 12):
        linha += [float(input())]
    matriz += [linha[:]]
    linha.clear()
soma = n = 0
t = 11
for p in range(0, 11):
    for j in range(0, t):
        soma += matriz[p][j]
        n+=1
    t -= 1

if tipo == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/n:.1f}')
