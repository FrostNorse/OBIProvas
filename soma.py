tamanho, valor = map(int, input().split())
seq = list(map(int, input().split()))
inicio = 0
retan = 0
final = 1
while inicio < tamanho:
    if sum(seq[inicio:final]) == valor:
        retan += 1
        if final > tamanho:
            break
        final += 1
    elif sum(seq[inicio:final]) > valor:
        inicio += 1
        final = inicio + 1
    else:
        final += 1
print(retan)
