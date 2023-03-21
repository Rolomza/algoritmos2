class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

# EJERCICIO 1 

def rotateLeft(Tree, avlnode):
    # El nuevo nodo raiz es el hijo derecho de la antigua raiz
    newRootNode = avlnode.rightnode
    if avlnode.parent != None:
        avlnode.parent.rightnode = newRootNode
    avlnode.rightnode = None
    # Si el nodo raiz anterior era la raiz del arbol, asignar su hijo derecho como nueva raiz del arbol
    if avlnode.parent == None:
        Tree.root = newRootNode
        newRootNode.parent = None
    else:
        # Sino asigno como padre del nuevo nodo raiz al padre del antiguo nodo raiz
        newRootNode.parent = avlnode.parent
    # Si el hijo derecho de la antigua raiz tenia un hijo izquierdo, este pasa a ser hijo derecho de la antigua raiz
    if newRootNode.leftnode != None:
        avlnode.rightnode = newRootNode.leftnode
        newRootNode.leftnode.parent = avlnode
    # El antiguo nodo raiz pasa a ser el hijo izquierdo del nuevo nodo raiz
    newRootNode.leftnode = avlnode
    avlnode.parent = newRootNode
    # Retorno la nueva raiz del arbol
    return newRootNode

def rotateRight(Tree,avlnode):
    # El nuevo nodo raiz es el hijo izquierdo de la antigua raiz
    newRootNode = avlnode.leftnode
    if avlnode.parent != None:
        avlnode.parent.leftnode = newRootNode
    avlnode.leftnode = None
    # Si el nodo raiz anterior era la raiz del arbol, asignar su hijo derecho como nueva raiz del arbol
    if avlnode.parent == None:
        Tree.root = newRootNode
        newRootNode.parent = None
    else:
        # Sino asigno como padre del nuevo nodo raiz al padre del antiguo nodo raiz
        newRootNode.parent = avlnode.parent
    # Si el hijo izquierdo de la antigua raiz tenia un hijo derecho, este pasa a ser hijo izquierdo de la antigua raiz
    if newRootNode.rightnode != None:
        avlnode.leftnode = newRootNode.rightnode
        newRootNode.rightnode.parent = avlnode
    # El antiguo nodo raiz pasa a ser el hijo derecho del nuevo nodo raiz
    newRootNode.rightnode = avlnode
    avlnode.parent = newRootNode
    # Retorno la nueva raiz del arbol
    return newRootNode

# EJERCICIO 2

def findHeight(node):
    # Caso base
    if node == None:
        return -1
    # Casos recursivos
    leftHeight = findHeight(node.leftnode)
    rightHeight = findHeight(node.rightnode)
    # Comparo las alturas y retorno recursivamente la mayor entre la izq y la der
    if leftHeight >= rightHeight:
        return 1 + leftHeight
    return 1 + rightHeight

def calcBalanceR(avlnode):
    # Caso base
    if avlnode == None:
        return 0
    # Casos recursivos
    leftHeight = calcBalanceR(avlnode.leftnode)
    rightHeight = calcBalanceR(avlnode.rightnode)
    # Calculo y actualizo el balance factor del nodo
    avlnode.bf = leftHeight - rightHeight
    # El retorno recursivo lleva implicito el valor de la altura del nodo mediante una funcion recursiva que calcula la altura del mismo
    return 1 + findHeight(avlnode)
    

def calculateBalance(AVLTree):
    if AVLTree.root == None:
        return
    # Llamado a funcion recursiva
    calcBalanceR(AVLTree.root)
    return AVLTree

# EJERCICIO 3

def reBalanceR(AVLTree, avlnode):
    # Caso base
    if avlnode == None:
        return
    # Detecto si el nodo tiene desbalance hacia la derecha
    if avlnode.bf < -1:
        # Se detecta si el hijo derecho tiene un hijo izquierdo
        if avlnode.rightnode.bf > 0:
            rotateRight(AVLTree, avlnode.rightnode)
            avlnode = rotateLeft(AVLTree, avlnode)
        else:
            avlnode = rotateLeft(AVLTree, avlnode)
        calculateBalance(AVLTree)
    # Detecto si el nodo tiene desbalance hacia la izquierda
    elif avlnode.bf > 1:
        # Se detecta si el hijo izquierdo tiene un hijo derecho
        if avlnode.leftnode.bf < 0:
            rotateLeft(AVLTree, avlnode.leftnode)
            avlnode = rotateRight(AVLTree, avlnode)
        else:
            avlnode = rotateRight(AVLTree, avlnode)
        calculateBalance(AVLTree)
    # Llamadas recursivas
    reBalanceR(AVLTree, avlnode.leftnode)
    reBalanceR(AVLTree, avlnode.rightnode)

def reBalance(AVLTree):
    if AVLTree.root == None:
        return
    calculateBalance(AVLTree)
    reBalanceR(AVLTree, AVLTree.root)
    return AVLTree


# EJERCICIO 4

def insert(AVLTree,element,key):
    current = AVLTree.root
    # Creo un nuevo nodo con la key y value ingresada por el usuario
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if current == None:
        AVLTree.root = newNode
        AVLTree.root.bf = 0
        return key
    recursiveInsert(newNode,AVLTree.root)
    # Una vez insertado el nodo, calculo el bf de cada nodo y balanceo desde el nodo insertado hasta la raiz del arbol
    updateBfAndBalance(AVLTree, newNode)
    

def recursiveInsert(newNode, treeNode):
    if newNode.key > treeNode.key:
        if treeNode.rightnode == None:
            treeNode.rightnode = newNode
            newNode.parent = treeNode
        else:
            recursiveInsert(newNode, treeNode.rightnode)
    else:
        if treeNode.leftnode == None:
            treeNode.leftnode = newNode
            newNode.parent = treeNode
        else:
            recursiveInsert(newNode, treeNode.leftnode)

def updateBfAndBalance(tree, node):
    if node == None:
        return
    calcBalanceR(node)
    if abs(node.bf) > 1:
        reBalanceR(tree, node)
        return
    # Llamado recursivo
    updateBfAndBalance(tree, node.parent)


# EJERCICIO 5

def delete(B,element):
    nodeToDelete = searchR(B.root,element)
    flag = 0
    if nodeToDelete == B.root:
        flag = 1
    if nodeToDelete == None:
        return

    if nodeToDelete.leftnode == None:
        transplant(B,nodeToDelete,nodeToDelete.rightnode)

    elif nodeToDelete.rightnode == None:
        transplant(B,nodeToDelete,nodeToDelete.leftnode)

    else:
        y = treeMinimum(nodeToDelete.rightnode)
        if y.parent != nodeToDelete:
            transplant(B,y,y.rightnode)
            y.rightnode = nodeToDelete.rightnode
            y.rightnode.parent = y
        transplant(B,nodeToDelete,y)
        y.leftnode = nodeToDelete.leftnode
        y.leftnode.parent = y
    if flag == 1:
        reBalance(B)
    else:
        updateBfAndBalance(B, nodeToDelete.parent)
    return nodeToDelete.key

def searchR(node, element):
    if node == None:
        return
    if node.value == element:
        return node
    right = searchR(node.rightnode, element)
    if right != None:
        return right
    left = searchR(node.leftnode, element)
    if left != None:
        return left

def treeMinimum(node):
    while node.leftnode != None:
        node = node.leftnode
    return node

def treeMaximum(node):
    while node.rightnode != None:
        node = node.rightnode
    return node

def transplant(B,u,v):
    if u.parent == None:
        B.root = v
    elif u == u.parent.leftnode:
        u.parent.leftnode = v
    else:
        u.parent.rightnode = v
    if v != None:
        v.parent = u.parent


# Implementaciones Binary tree: search, insert, delete, deleteKey, access, update

def search(B, element):
    current = B.root
    if current.value == element:
        return current.key
    if current == None:
        return None
    try:
        return searchR(current, element).key
    except:
        return


def searchKey(B, key):
    current = B.root
    if current.key == key:
        return current
    if current == None:
        return
    return searchKeyR(current, key)


def searchKeyR(node, key):
    if node.key == key:
        return node
    if node.key > key:
        if node.leftnode != None:
            return searchKeyR(node.leftnode, key)
        return
    else:
        if node.rightnode != None:
            return searchKeyR(node.rightnode, key)
        return

def access(B, key):
    current = searchKey(B, key)
    if current == None:
        return
    return current.value

def update(B, element, key):
    current = searchKey(B, key)
    if current == None:
        return
    current.value = element
    return current.key

# Recorrer arboles

def traverseInOrder(B):
    if B.root == None:
        return
    recursiveInOrderTreeWalk(B.root)

def recursiveInOrderTreeWalk(treeNode):
    if treeNode != None:
        recursiveInOrderTreeWalk(treeNode.leftnode)
        print(treeNode.value)
        recursiveInOrderTreeWalk(treeNode.rightnode)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.rightnode, level+1)
        print(' ' * 4 * level + '->', node.key, f"(bf={node.bf})")
        print_tree(node.leftnode, level+1)