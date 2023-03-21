from avltree import *

myAvlTree = AVLTree()
#Root
insert(myAvlTree, 20, 20)
insert(myAvlTree,10,10)
insert(myAvlTree,25,25)
insert(myAvlTree,30,30)
print_tree(myAvlTree.root)

print('Inserto')

insert(myAvlTree,40,40)
insert(myAvlTree,60,60)

print(myAvlTree.root.value)
# print(myAvlTree.root.leftnode.value)
print_tree(myAvlTree.root)


