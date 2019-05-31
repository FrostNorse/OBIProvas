linha, colunas = map(int, input().split())
parede = []
index = 0
mudou = False


for k in range(linha):
    parede.append(list(map(str, input().split())))


while index != linha:
    mudou = False
    for j in range(colunas):
        if index != 0:
            if parede[index-1][j] == 'o' and parede[index][j] != '#':
                parede[index][j] = 'o'
        if index % 2 == 0 and index != linha - 1:
            if parede[index+1][j] == '#' and parede[index][j] == 'o':
                if j < colunas - 1 and parede[index][j+1] != 'o' and '#':
                    parede[index][j+1] = 'o'
                    mudou = True
                if j > 0 and parede[index][j-1] != 'o' and '#':
                    parede[index][j-1] = 'o'
                    mudou = True
                if mudou:
                    break
    if not mudou:
        index += 1


for k in range(linha):
    print(str(parede[k]).replace("[", "").replace(",", "").replace("]", "").replace("'", "").replace(" ", ""))
