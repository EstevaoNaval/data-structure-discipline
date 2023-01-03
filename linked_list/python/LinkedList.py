class Node:
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
    
    def get__data(self): return self.__data

    def get__next(self): return self.__next

    def set__data(self, data): self.__data = data

    def set__next(self, next): self.__next = next

class LinkedList:
    def __init__(self, data):
        self.__root = Node(data)
    
    def get__root(self): return self.__root

    def set__root(self, root): self.__root = root

    def print(self):
        self.__print(self.__root)
    
    def __print(self, root):
        if(root is None): return

        print(root.get__data())
        self.__print(root.get__next())
    
    def printReverse(self):
        self.__printReverse(self.__root)

    def __printReverse(self, root):
        if(root is None): return

        self.__printReverse(root.get__next())
        print(root.get__data())
    
    def insert(self, data):
        self.__root = self.__insert(self.__root, data)

    def __insert(self, root, data):
        node = Node(data)
        node.set__next(root)

        return node