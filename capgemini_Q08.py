v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

v[1] = 1
v[2] = 2
v[3] = 3
v[4] = 4
v[5] = 5
v[6] = 6
v[7] = 8
v[8] = 8
v[9] = 9
v[10] = 10

temValoresRepetidos = False

for i in range(1, 10):
    for j in reversed(range(1, 10)):
        if(v[i] == v[j] and i != j):
            temValoresRepetidos = True


print("EXISTEM VALORES REPETIDOS?  ", temValoresRepetidos)
