from torch.ao.quantization.backend_config.backend_config import ROOT_NODE_GETTER_DICT_KEY


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.data = data
        elif data:
            node = Node(data)
            self.root = node #raiz
        else:
            self.root = None

    def simetric_transversal(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_transversal(node.left)
            print(node)
        if node.right:
            self.simetric_transversal(node.right)


    def postorder_transversal(self,node=None):
        if node is None:
            node =self.root

        if node.left:
            self.postorder_transversal(node.left)
        if node.right:
            self.postorder_transversal(node.right)
            print(node)


    def hight(self,node=None):
        if node is None:
            node =self.root
        hleft = 0
        hright = 0
        if node.left:
            self.hight(node.left)
        if node.right:
            self.hight(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

class BinarySearchTree(BinaryTree):

    def insert(self,value):
        parent =None
        x = self.root

        while(x):
            parent = x

            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search (self,value):
        return self._search(value, self.root)

    def _search(self,value,node):
        if node is None or none.data ==value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value,node.left)
        return self._search(value,node.right)

    def min(self, node=ROOT):
        if node ==ROOT
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self):
        if node ==ROOT
            node=self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self,value,node=ROOT):
        if node == ROOT:
            node = self.root

        if node is None:
            return node

        if value < node.data:
            node.left = self.remove(value,node.left)

        elif  value > node.data:
            node.right = self.remove(value,node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute =self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute,node.right)

















if __name__ == "__main__":
    tree = BinaryTree(5)  # Cria uma árvore binária com a raiz 5
    tree.root.left = Node(3)  # Adiciona um nó à esquerda com valor 3
    tree.root.right = Node(6)  # Adiciona um nó à direita com valor 6

    print(tree.root)         # Saída: 5
    print(tree.root.left)    # Saída: 3
    print(tree.root.right)   # Saída: 6
