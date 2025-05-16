# Singly Linked List – Lista Simplesmente Encadeada
# Apenas com as operações básicas que vamos precisar para filas nesse momento.
# insert_at_top e remove_at_top

class Node:
    def __init__(self, data):
        self.data = data    # Valor do nó
        self.next = None    # Ponteiro para o próximo nó

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None     # Ponteiro para o topo da Lista
        self.tail = None
        self.size = 0       # Tamanho da Lista

    def insert_at_top(self, data):
        """
        Insere um novo nó no topo da lista (top).
        """
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1 

    def remove_at_top(self):
        """
        Remove o nó do início da lista e retorna seu valor.
        Se a lista estiver vazia, levanta um erro.
        """
        if self.head is None:
            raise IndexError("Estrutura Vazia - Impossível remover elemento")
        
        removed_data = self.head.data    # Guarda o valor que está no topo e será removido
        self.head = self.head.next        # Top agora aponta para o próximo nó
                                        # Garbage Colector vai destruir o nó solto
        if self.head is None:
            self.tail = None
        self.size -= 1                  
        return removed_data

    def is_empty(self):
        """
        Verifica se a lista está vazia.
        """
        return self.size == 0

    def peek_start(self):
        """
        Retorna o valor do topo, sem removê-lo.
        """
        if self.head is None:
            raise IndexError("Estrutura Vazia - Impossível espiar")
        return self.head.data

    def peek_end(self):
        if self.tail is None:
            raise IndexError("Estrutura Vazia - Impossível espiar")
        return self.tail.data


# Implementação da fila usando a Lista Simplesmente Encadeada

class Queue:
    """
    Classe Queue (fila) implementada sobre a Lista Simplesmente Encadeada.
    """
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def enqueue(self, data):
        """
        Insere (enqueue) um novo elemento na fila.
        """
        self.singly_linked_list.insert_at_top(data)
        print(f"{data} entrou na fila com sucesso.")

    def dequeue(self):
        """
        Remove da fila (dequeue) o elemento do topo da fila e retorna seu valor.
        """
        data = self.singly_linked_list.remove_at_top()
        print(f"{data} saiu da fila com sucesso.")
        return data

    def peek_start(self):
        """
        Espia (peek_start) o elemento do início da fila sem removê-lo.
        """
        data = self.singly_linked_list.peek_start()
        print(f"O elemento no início da fila é: {data}")
        return data
    
    def peek_end(self):
        """
        Espia (peek_end) o elemento do final da fila sem removê-lo.
        """
        data = self.singly_linked_list.peek_end()
        print(f"O elemento no final da fila é: {data}")
        return data

    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """
        return self.singly_linked_list.is_empty()
    
    def size(self):
        """
        retorna o tamanho da fila.
        """
        print (f"O tamanho da fila é: {self.singly_linked_list.size}")
        return self.singly_linked_list.size
    
    def __str__(self):
        """
        Método mágico para representar a fila no formato:

        1 (Início da Fila) - 5 - 3 (Fim da Fila)

        Mostra a ligação interna entre os nós da fila.
        """
        if self.singly_linked_list.head is None:
            return "fila vazia"

        linhas = []
        atual = self.singly_linked_list.head  # Começa pelo topo
        index = 0  # Para saber se é o primeiro (topo) ou último (base)

        while atual is not None:
            if index == 0:
                # Primeiro elemento é o topo
                linhas.append(f"{atual.data} (Início da Fila)")
            else:
                # Elementos intermediários, só valor
                linhas.append(f"{atual.data}")

            atual = atual.next
            if atual is not None:
                linhas.append("-")  # Adiciona seta entre os nós
            index += 1

        # Após montar todas as linhas, indicamos que o último é a base
        if "->" in linhas[-1]:
            # Se terminou com seta removemos
            linhas.dequeue()

        # Marca a base no último elemento (se não for igual ao topo)
        if index > 1:
            # Último elemento é a base (precisamos localizar a última linha com número)
            for i in range(len(linhas) - 1, -1, -1):
                if linhas[i] != "-":
                    linhas[i] += " (Fim da Fila)"
                    break

        return " ".join(linhas)


# Testando a fila

if __name__ == "__main__":
    fila = Queue()
    
    # Enfileirando elementos
    fila.enqueue("Cebola")
    fila.enqueue("Salada")
    fila.enqueue("Melancia")

    # Espiando o ínicio da fila
    fila.peek_start()
    
    # Espiando o fim da fila
    fila.peek_end()

    # Remove da fila elementos
    fila.dequeue()
    fila.dequeue()

    # Verificando se está vazia
    print("A fila está vazia?" , fila.is_empty())

    # Último dequeue
    fila.dequeue()

    # Tentando espiar uma fila vazia (gera erro)
    try:
        fila.peek_start()
    except IndexError as e:
        print(e)

    fila.size()
    
    print("\n Enfileirar números 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    print(fila)  # Deve mostrar 10 (Início da Fila) - 20 - 10 (Fim da Fila)
    fila.size()
