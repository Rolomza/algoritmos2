from avltree import *

myAvlTree = AVLTree()
insert(myAvlTree, 10, 10)
insert(myAvlTree, 15, 15)
insert(myAvlTree, 12, 12)
insert(myAvlTree, 20, 20)

traversePreorder(myAvlTree.root)

rotateLeft(myAvlTree,myAvlTree.root)

print('Arbol rotado hacia la izquierda')
traversePreorder(myAvlTree.root)
