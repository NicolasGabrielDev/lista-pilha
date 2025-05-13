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

    aberturas = ["{", "(", "["]
    fechamentos = ["}", ")", "]"]
    correspondentes = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    for l in expression:
        if l in aberturas:
            pilha.push(l)
        elif l in fechamentos:
            if not pilha.is_empty() and correspondentes[pilha.peek()] == l:
                pilha.pop()
            else:
                return False

    return pilha.is_empty()

# Teste
print(is_balanced("[{}()]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
