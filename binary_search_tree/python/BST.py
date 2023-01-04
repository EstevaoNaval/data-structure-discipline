import sys

sys.path.append('./binary_tree/python/')

from BinaryTree import Node

class BST:
    def __init__(self, data=None):
        if(data):
            self.__root = Node(data, None, None)
        else:
            self.__root = None

    def get__root(self): return self.__root

    def set__root(self, root): self.__root = root
    
    def sortedPrint(self):
        self.__inOrderTransversal(self.get__root())

    def __preOrderTransversal(self, root):
        if(root is None): return

        print(root.get__data())
        self.__preOrderTransversal(root.get__leftNode())
        self.__preOrderTransversal(root.get__rightNode())

    def __inOrderTransversal(self, root):
        if(root is None): return

        self.__inOrderTransversal(root.get__leftNode())
        print(root.get__data())
        self.__inOrderTransversal(root.get__rightNode())
    
    def __postOrderTransversal(self, root):
        if(root is None): return

        self.__postOrderTransversal(root.get__leftNode())
        self.__postOrderTransversal(root.get__rightNode())
        print(root.get__data())

    def search(self, data):
        self.__search(self.get__root(), data)
    
    def __search(self, root, data):
        if(root is None or root.get__data() == data): return root

        if(data < root.get__data()):
            resp = self.__search(root.get__leftNode(), data)
        elif(data > root.get__data()):
            resp = self.__search(root.get__rightNode(), data)

        return resp
    
    def insert(self, data):
        self.set__root(self.__insert(self.get__root(), data))
    
    def __insert(self, root, data):
        if(root is None): return Node(data, None, None)

        if(data < root.get__data()):
            root.set__leftNode(self.__insert(root.get__leftNode(), data))
        elif(data > root.get__data()):
            root.set__rightNode(self.__insert(root.get__rightNode(), data))
        
        return root

    def remove(self, data):
        self.set__root(self.__remove(self.get__root(), data))

    def __remove(self, root, data):
        if(root is None): return root

        if(data < root.get__data()):
            root.set__leftNode(self.__remove(root.get__leftNode(), data))
        elif(data > root.get__data()):
            root.set__rightNode(self.__remove(root.get__rightNode(), data))
        else:
            if(root.get__leftNode() is None and root.get__rightNode() is None):
                del root
                root = None
            elif(root.get__leftNode() is None  or root.get__rightNode() is None):
                aux = root

                if(root.get__leftNode()): root = root.get__leftNode()
                else: root = root.get__rightNode()

                del aux
            else:
                filho = root.get__leftNode()

                while(filho.get__rightNode()): filho = filho.get__rightNode()
                root.set__data(filho.get__data())
                filho.set__data(data)

                root.set__leftNode(self.__remove(root.get__leftNode(), data))

        return root
