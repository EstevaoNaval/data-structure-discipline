class Node:
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next
    
    def get__data(self): return self.__data

    def get__next(self): return self.__next

    def set__data(self, data): self.__data = data

    def set__next(self, next): self.__next = next

class LinkedList:
    def __init__(self, data=None):
        if(data):
            self.__root = Node(data)
        else:
            self.__root = None
    
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

    def insertEnd(self, data):
        self.__root = self.__insertEnd(self.__root, data)
    
    def __insertEnd(self,root, data):
        if(root is None): return self.__insert(root, data)
        
        root.set__next(self.__insertEnd(root.get__next(), data))

        return root

    def insertSorted(self, data):
        self.__root = self.__insertSorted(self.__root, data)

    def __insertSorted(self, root, data):
        if(root is None or data <= root.get__data()):
            return self.__insert(root, data)
        
        root.set__next(self.__insertSorted(root.get__next(), data))

        return root

    