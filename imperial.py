tamanho = int(input())
sequencia = []
maior1 = 0
maior2 = 0
contadorNum = 0
contadorMaior = 0
contadorSeq = 0
ultimo = 0


for k in range(tamanho):
    sequencia.append(int(input()))


for i in range(tamanho):
    for j in sequencia[i:]:
            if j == sequencia[i]:
                contadorNum += 1
    if contadorNum > contadorMaior:
        maior1 = sequencia[i]
        contadorMaior = contadorNum
    contadorNum = 0


contadorMaior = 0


for i in range(tamanho):
    for j in sequencia[i:]:
            if j == sequencia[i]:
                contadorNum += 1
    if contadorNum > contadorMaior and maior1 != sequencia[i]:
        maior2 = sequencia[i]
        contadorMaior = contadorNum
    contadorNum = 0


for t in sequencia:
    if (t == maior1 or t == maior2) and t != ultimo:
        ultimo = t
        contadorSeq += 1


print(contadorSeq)
