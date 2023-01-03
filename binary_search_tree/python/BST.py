import sys

sys.path.append('./binary_tree/python/')

from BinaryTree import Node

class BST:
    def __init__(self, data=None):
        self.__root = Node(data, None, None)

    def get__root(self): return self.__root

    def set__root(self, root): self.__root = root
    
    def print(self):
        self.__postOrderTransversal(self.__root)

    def __preOrderTransversal(self, root):
        if(root is None): return

        print(root.data)
        self.__preOrderTransversal(root.leftNode)
        self.__preOrderTransversal(root.rightNode)

    def __inOrderTransversal(self, root):
        if(root is None): return

        self.__inOrderTransversal(root.leftNode)
        print(root.data)
        self.__inOrderTransversal(root.rightNode)
    
    def __postOrderTransversal(self, root):
        if(root is None): return

        self.__postOrderTransversal(root.leftNode)
        self.__postOrderTransversal(root.rightNode)
        print(root.data)
