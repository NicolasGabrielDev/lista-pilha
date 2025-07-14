def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def two_sum_v1(numeros, alvo):
    for i, valor_atual in enumerate(numeros):
        for j, valor in enumerate(numeros):
            if j != i and valor_atual + valor == alvo:
                return [i, j]
    raise Exception("Nenhum resultado válido")

def two_sum_v2(numeros, alvo):
    numeros = [(valor, i) for i, valor in enumerate(numeros)]
    
    quicksort(numeros)

    num_1 = numeros[0]
    num_1_pos = 0

    num_2 = numeros[-1]
    num_2_pos = len(numeros) - 1

    while True:
        soma = num_1[0] + num_2[0]
        if soma == alvo:
            return [num_1[1], num_2[1]]
        if soma < alvo:
            num_1_pos += 1
            num_1 = numeros[num_1_pos]
        else:
            num_2_pos -= 1
            num_2 = numeros[num_2_pos]
            
def two_sum_v3(numeros, alvo):
    # mapeia cada valor ao seu índice em `numeros`

    indice_por_valor = {}  

    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i
            
if __name__ == "__main__":

    numeros = [2, 7, 11, 15]

    alvo = 9

    resultado_v1 = two_sum_v1(numeros, alvo)
    print("V1:", resultado_v1)  # Exemplo de saída: [0, 1]

    resultado_v2 = two_sum_v2(numeros, alvo)
    print("V2:", resultado_v2)  # Exemplo de saída: [0, 1]

    resultado_v3 = two_sum_v3(numeros, alvo)
    print("V3:", resultado_v3)  # Exemplo de saída: [0, 1]
