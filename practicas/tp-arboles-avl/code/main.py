from avltree import *

myAvlTree = AVLTree()
#Root
insert(myAvlTree, 20, 20)

#SubArbol Izq
insert(myAvlTree, 10, 10)
insert(myAvlTree, 5, 5)
#insert(myAvlTree, 5, 5)
#insert(myAvlTree, 2, 2)

#SubArbol Der
#insert(myAvlTree, 25, 25)
#insert(myAvlTree, 23,23)
#insert(myAvlTree, 40, 40)
#insert(myAvlTree, 50, 50)

# Tree Re-balance

print('Initial Tree root:', myAvlTree.root.value)
print('Initial root rightnode', myAvlTree.root.leftnode.value)
print('Initial root rightnode', myAvlTree.root.leftnode.leftnode.value)


rotateRight(myAvlTree, myAvlTree.root)

print('New root', myAvlTree.root.value)
print('left', myAvlTree.root.leftnode.value)
print('right', myAvlTree.root.rightnode.value)

print('papa de left', myAvlTree.root.leftnode.parent.value)
print('papa de right', myAvlTree.root.rightnode.parent.value)