numPosic, numMov = map(int, input().split())
cofre = list(map(int, input().split()))
mov = list(map(int, input().split()))
actualIndex = 0
digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
digitos[cofre[0]] += 1
cont = 0
while cont < len(mov)-1:
    if actualIndex < mov[cont+1]:
        while actualIndex + 1 < mov[cont+1]:
            digitos[cofre[actualIndex+1]] += 1
            actualIndex += 1
    else:
        while actualIndex >= mov[cont+1]:
            digitos[cofre[actualIndex-1]] += 1
            actualIndex -= 1
    cont += 1
print(str(digitos).strip("[]").replace(",", ""))
