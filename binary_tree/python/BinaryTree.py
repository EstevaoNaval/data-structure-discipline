class Node:
    def __init__(self, data = None, leftNode = None, rightNode=None):
        self.__data = data
        self.__leftNode = leftNode
        self.__rightNode = rightNode
    
    def get__data(self): return self.__data
    
    def get__leftNode(self): return self.__leftNode
    
    def get__rightNode(self): return self.__rightNode

    def set__data(self, data): self.__data = data

    def set__leftNode(self, leftNode): self.__leftNode = leftNode

    def set__rightNode(self, rightNode): self.__rightNode = rightNode

class BinaryTree:
    def __init__(self, rootData = None):
        self.root = Node(rootData)
    
    def print(self):
        self._inOrderTransversal(self.root)
    
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
        return self.__search(self.root, data)

    def __search(self, root, data):
        if(root is None or root.get__data() == data): return root

        result = self.__search(root.get__leftNode(), data)
        if(result): return result
        return self.__search(root.get__rightNode(), data)
    
    def insert(self, rootData, left=None,right=None):
        self.__insert(rootData, left, right)

    def __insert(self, rootData, left=None, right=None):
        root = self.search(rootData)
        
        if(root is None):
            raise Exception("Node {} doesn't exist".format(rootData)) 

        if(left and root.get__leftNode() is None):
            root.set__leftNode(Node(left)) 
        
        if(right and root.get__rightNode() is None):
            root.set__rightNode(Node(right))

    def remove(self, data):
        self.root = self.__remove(self.root, data)
    
    def __remove(self, root, data):
        if(root is None): return root

        root.set__leftNode(self.__remove(root.get__leftNode(), data))
        if(root.get__data() == data):
            if(root.get__leftNode() is None and root.get__rightNode() is None):
                del root
                root = None
            elif(root.get__leftNode() and root.get__rightNode() is None):
                aux = root
                root = root.get__leftNode()
                del aux
            elif(root.get__leftNode() is None and root.get__rightNode()):
                aux = root
                root = root.get__rightNode()
                del aux
            else:
                filho = root.get__leftNode()
                while(filho.get__rightNode()): filho = filho.get__rightNode()
                root.set__data(filho.get__data()) 
                filho.set__data(data)
                root.set__leftNode(self.__remove(root.get__leftNode(), data))

            return root
        root.set__rightNode(self.__remove(root.get__rightNode(), data))
        return root