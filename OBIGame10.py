espaco = int(input())
nave = int(input())
aviao = int(input())
mov = 0
while aviao != nave:
    mov += 1
    aviao +=1
    if aviao > espaco:
        aviao %= espaco
print(mov)
