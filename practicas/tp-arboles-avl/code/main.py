from avltree import *

myAvlTree = AVLTree()
#Root
insert(myAvlTree, 20, 20)

#SubArbol Izq
#insert(myAvlTree, 10, 10)
#insert(myAvlTree, 5, 5)
#insert(myAvlTree, 5, 5)
#insert(myAvlTree, 2, 2)

#SubArbol Der
insert(myAvlTree, 25, 25)
#insert(myAvlTree, 23,23)
insert(myAvlTree, 40, 40)
#insert(myAvlTree, 50, 50)

# Tree Re-balance

print('Initial Tree root:', myAvlTree.root.value)
print('Initial root rightnode', myAvlTree.root.rightnode.value)
print('Initial root rightnode', myAvlTree.root.rightnode.rightnode.value)

reBalance(myAvlTree)

print(myAvlTree.root.value)

# print('Final tree root',myAvlTree.root.value)
# print('Initial root leftnode', myAvlTree.root.leftnode.value)
# print('Initial root rightnode', myAvlTree.root.rightnode.value)



