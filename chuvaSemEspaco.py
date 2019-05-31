linha, colunas = map(int, input().split())
parede = []
index = 0
mudou = False


for k in range(linha):
    parede.append(input())


for k in range(linha):
    while parede[k].count(" ") != colunas - 1:
        parede[k] = parede[k].replace("..", ". .").replace(".o", ". o").replace("o.", "o .").replace(".#", ". #").replace(
            "#.", "# .").replace("##", "# #")
    parede[k] = list(parede[k].split())


while index != linha:
    mudou = False
    for j in range(colunas):
        if index != 0:
            if parede[index-1][j] == 'o' and parede[index][j] != '#':  # em cima
                parede[index][j] = 'o'
        if index % 2 == 0 and index != linha - 1:
            if parede[index+1][j] == '#' and parede[index][j] == 'o':  # em baixo
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
