from avltree import *

myAvlTree = AVLTree()
#Root
insert(myAvlTree, 20, 20)

#SubArbol Izq
insert(myAvlTree, 10, 10)
insert(myAvlTree, 8, 8)
insert(myAvlTree, 5, 5)
# insert(myAvlTree, 2, 2)

#SubArbol Der
#insert(myAvlTree, 25, 25)
#insert(myAvlTree, 23,23)
#insert(myAvlTree, 40, 40)
#insert(myAvlTree, 50, 50)

# Tree Re-balance

print_tree(myAvlTree.root)

reBalance(myAvlTree)

print_tree(myAvlTree.root)



