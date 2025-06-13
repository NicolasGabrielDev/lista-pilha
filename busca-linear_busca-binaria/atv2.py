from random import randint
from quicksort import quicksort

citacoes = []

print("Informe o número de artigos")
n = int(input())

for _ in range(n):
    citacoes.append(randint(0, 20))

quicksort(citacoes)

print("Notas do Autor: ")
print(citacoes)

# Busca Linear

flag = True
aux = n - 1
i = 1
while flag and aux >= 0:
    if citacoes[aux] < i:
        flag = False 
        print(f"O índice H do autor é: {i - 1}")
        break
    aux -= 1
    i += 1

if flag:
    print(f"O índice H do autor é: {i - 1}")


left = 0
right = n - 1
flag = True

while left <= right and flag:
    mid = (left + right) // 2
    if citacoes[mid] < mid:
        print(f"Valor encontrado na Busca Binária. Seu índice é: {mid}")
        flag = False
        break
    else:
        if citacoes[mid] >= mid:
            right = mid - 1
        else:
            left = mid + 1