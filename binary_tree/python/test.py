from BinaryTree import BinaryTree

binTree = BinaryTree(35)
binTree.insert(35, None, 45)
binTree.insert(35, 75, None)
binTree.insert(75, 63, None)
binTree.insert(63, 55, None)
binTree.insert(75, None, 69)

binTree.print()

binTree.remove(35)
binTree.remove(45)
binTree.remove(69)

binTree.insert(75,None,99)
binTree.insert(63,None,65)
