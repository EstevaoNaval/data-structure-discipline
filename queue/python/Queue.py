class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None
    
    def get__data(self):
        return self.__data
    
    def get__next(self):
        return self.__next

    def set__next(self, next):
        self.__next = next
    
class Queue:
    def __init__(self, data=None):
        if(data):
            self.__first = Node(data)
            self.__last = self.__first
            self.__size = 1
        else:
            self.__first = None
            self.__last = None
            self.__size = 0
    
    def peek(self):
        if(self.__size <= 0):
            try:
                raise IndexError()
            except IndexError:
                print("This queue is empty!")
                return None
        
        return self.__first.get__data()
    
    def push(self, data):
        self.__size += 1
        return self.__push(self.__first, data)

    def __push(self, root, data):
        if(root is None):
            self.__first = Node(data)
            self.__last = self.__first
            return self.__first
        
        self.__last.set__next(Node(data))
        self.__last = self.__last.get__next()

        return self.__last.get__data()

    def pop(self):
        if(self.__len__() <= 0):
            return None
        
        data = self.peek()
        
        aux = self.__first.get__next()
        del self.__first
        self.__first = aux

        self.__size -= 1

        return data


    def __len__(self):
        return self.__size
    
