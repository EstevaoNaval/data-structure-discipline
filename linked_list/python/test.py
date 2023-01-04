from LinkedList import LinkedList

list = LinkedList()
list.insert(35)
list.insert(12)
list.insert(56)
list.insert(21)
list.insert(49)
list.insert(55)
list.insert(49)
list.insert(100)

print()
print(list.search(100).get__data())
print(list.search(56).get__data())

print()

list.print()
print()

list.remove(12)
list.remove(100)
list.remove(49)

print(list.search(100))
print()

list.print()