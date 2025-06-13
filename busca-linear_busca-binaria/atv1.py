from random import randint
from quicksort import quicksort

arr = []

print("Informe o Tam do Array")
n = int(input())

for _i in range(n):
    arr.append(randint(1, 1000))

quicksort(arr)
print("Array gerado:")
print(arr)

print("Informe o Número a Pesquisar")
search = int(input())

# Com Busca Linear

flag = True
for index, item in enumerate(arr):
    if item == search:
        print(f"Valor encontrado. Seu índice é: {index}")
        flag = False
        break

    if item > search:
        print(f"Valor não encontrado. Seu índice para adicionar é: {index}")
        flag = False
        break

if flag:
    if arr[0] > search:
        print(f"Valor não encontrado. Seu índice correto é: {0}")
    else:
        print(f"Valor não encontrado. Seu índice correto é: {n}")

# Busca Binária

left = 0
right = n - 1
flag = True

while left <= right and flag:
    mid = (left + right) // 2
    if arr[mid] == search:
        print(f"Valor encontrado na Busca Binária. Seu índice é: {mid}")
        flag = False
        break
    else:
        if arr[mid] > search:
            right = mid - 1
        else:
            left = mid + 1

if flag:
    print(f"Índice para ser adicionado: {left}")
    





