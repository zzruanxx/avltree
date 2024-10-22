class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        # Inserção padrão em árvore binária de busca
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Atualiza a altura do nó ancestral
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Verifica o fator de balanceamento
        balance = self.get_balance(root)

        # Casos de rotação
        # Caso Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Caso Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Caso Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


# Exemplo de uso
avl = AVLTree()
root = None

# Inserindo valores na árvore AVL
values = [10, 20, 30, 40, 50, 25]
for value in values:
    root = avl.insert(root, value)

# Exibindo a árvore em pré-ordem
print("Pre-order traversal da árvore AVL:")
avl.pre_order(root)
