from stack import SinglyLinkedList

class Queue:
    def __init__(self):
        self.elements = SinglyLinkedList()
        self.aux = SinglyLinkedList()

    def enqueue(self, data):
        self.elements.insert_at_top(data)

    def dequeue(self):
        if self.elements.is_empty():
            raise IndexError("Fila está vazia")
        
        while not self.elements.is_empty():
            self.aux.insert_at_top(self.elements.delete_from_top())
        
        el = self.aux.delete_from_top()

        while not self.aux.is_empty():
            self.elements.insert_at_top(self.aux.delete_from_top())

    def is_empty(self):
        return self.elements.is_empty()

fila = Queue()
    
# Enfileirando elementos
fila.enqueue("Cebola")
fila.enqueue("Salada")
fila.enqueue("Melancia")

# Remove da fila elementos
fila.dequeue()
fila.dequeue()

# Verificando se está vazia
print("A fila está vazia?" , fila.is_empty())

# Último dequeue
fila.dequeue()

print("\n Enfileirar números 10, 20, 30")
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila)  # Deve mostrar 10 (Início da Fila) - 20 - 10 (Fim da Fila)