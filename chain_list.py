class Chain:
    def __init__(self, content):
        self.content = content
        self.next = None

class ChainList:
    def __init__(self):
        self.head = None

    def append(self, content):
        new_cell = Chain(content)
        if not self.head:
            self.head = new_cell
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_cell

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            popped_content = self.head.content
            self.head = None
            return popped_content
        else:
            current = self.head
            while current.next.next:
                current = current.next
            popped_content = current.next.content
            current.next = None
            return popped_content

# Test de la classe ChainList
chain_list = ChainList()

chain_list.append("Première cellule")
chain_list.append("Deuxième cellule")
chain_list.append("Troisième cellule")

print("Contenu de la chaîne :")
current = chain_list.head
while current:
    print(current.content)
    current = current.next

popped_content = chain_list.pop()
print(f"\nCellule supprimée : {popped_content}")

print("\nContenu après suppression :")
current = chain_list.head
while current:
    print(current.content)
    current = current.next
