dona = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = dona - (filho1 + filho2)
if filho1 > filho2 and filho3:
    print(filho1)
elif filho2 > filho3 and filho1:
    print(filho2)
else:
    print(filho3)
