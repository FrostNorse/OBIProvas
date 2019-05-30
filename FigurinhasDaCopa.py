Espaco, carimbada, figurinha = map(int, input().split())
carimbos = list(map(int, input().split()))
compradas = list(map(int, input().split()))
indexCarimbo = 0
indexComprada = 0
falta = len(carimbos)
while True:
    while True:
        if carimbos[indexCarimbo] == compradas[indexComprada]:
            falta -= 1
            indexComprada = 0
            break
        indexComprada += 1
        if indexComprada == len(compradas):
            indexComprada = 0
            break
    indexCarimbo += 1
    if indexCarimbo == len(carimbos):
        break
print(falta)