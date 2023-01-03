from BST import BST

bst = BST(100)
bst.insert(35)
bst.insert(95)
bst.insert(125)
bst.insert(12)
bst.insert(55)
bst.insert(150)
bst.insert(102)

bst.sortedPrint()
print("\n")

bst.remove(55)
bst.remove(100)
bst.remove(35)

bst.sortedPrint()