from avltree import *
myAvlTree = AVLTree()
#Root
insert(myAvlTree,20,20)
insert(myAvlTree,25,25)
insert(myAvlTree,10,10)
insert(myAvlTree,8,8)
insert(myAvlTree,5,5)

print_tree(myAvlTree.root)

print()
print('Prueba de implementacion delete()')
delete(myAvlTree,8)
print_tree(myAvlTree.root)



