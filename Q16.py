
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Função para adicionar elementos à lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Função para imprimir a lista
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def inverterNos(L):

    Prev = None
    Current = L.head

    while Current != None:
        Saved = Current.next  # Salva o próximo nó
        Current.next = Prev  # Inverte a referência
        Prev = Current  # Atualiza Prev para o nó atual
        Current = Saved  # Avança para o próximo nó


    L.head = Prev
    return L
# Criar e inverter uma lista
lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

print("Lista original:")
lista.print_list()

# Inverter a lista
inverterNos(lista)

print("Lista invertida:")
lista.print_list()

