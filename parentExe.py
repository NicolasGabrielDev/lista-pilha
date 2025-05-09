# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    for l in expression:
        pilha.push(l)

    if pilha.size() == 0:
        return False
    
    dic = {
        "{": 0,
        "}": 0,
        "[": 0,
        "]": 0,
        "(": 0,
        ")": 0
    }

    while not pilha.is_empty():
        el = pilha.pop()
        if el in dic:
            dic[el] += 1
    
    if dic["{"] != dic["}"]:
        return False

    if dic["["] != dic["]"]:
        return False

    if dic["("] != dic[")"]:
        return False
    
    return True
    


# Teste
print(is_balanced("[{}()]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
