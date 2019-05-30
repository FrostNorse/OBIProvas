tamanho = int(input())
sequencia = list(map(int, input().split()))
escadinhas = 1
if tamanho <= 2:
    print("1")
else:
    ultimaEscada = sequencia[0] - sequencia[1]
    indice = 1
    while indice < tamanho - 1:
        if sequencia[indice] - sequencia[indice + 1] != ultimaEscada:
            escadinhas += 1
            ultimaEscada = sequencia[indice] - sequencia[indice + 1]
        indice += 1
    print(escadinhas)
