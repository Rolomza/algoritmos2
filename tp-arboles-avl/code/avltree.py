import linkedlist
import myqueue

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
    Tree.root = avlnode.rightnode
    avlnode.rightnode.parent = None

    if Tree.root.leftnode != None:
        avlnode.rightnode = Tree.root.leftnode
        Tree.root.leftnode.parent = avlnode

    Tree.root.leftnode = avlnode
    avlnode.parent = Tree.root



    return Tree.root






















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

def insert(B,element,key):
    current = B.root
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if current == None:
        B.root = newNode
        return key
    recursiveInsert(newNode,B.root)
    

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

def delete(B,element):
    nodeToDelete = searchR(B.root,element)
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

    return nodeToDelete.key


def deleteKey(B, key):
    current = searchKey(B, key)
    if current == None:
        return
    if current.leftnode == None:
        transplant(B, current, current.rightnode)
    elif current.rightnode == None:
        transplant(B, current, current.leftnode)
    else:
        nodeMin = treeMinimum(current.rightnode)
        if nodeMin.parent != current:
            transplant(B, nodeMin, nodeMin.rightnode)
            nodeMin.rightnode = current.rightnode
            nodeMin.parent.rightnode = nodeMin
        transplant(B, current, nodeMin)
        nodeMin.leftnode = current.leftnode
        nodeMin.leftnode.parent = nodeMin
    return current.key

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

def traversePreorder(root):
    if root:
        print(root.value),
        traversePreorder(root.leftnode)
        traversePreorder(root.rightnode)

def traverseBreadFirst(B):
    queue = linkedlist.LinkedList()
    valuesQueue = linkedlist.LinkedList()
    myqueue.enqueue(queue,B.root)

    while queue.head != None:
        node = myqueue.dequeue(queue)
        myqueue.enqueue(valuesQueue,node.value)

        if node.leftnode != None:
            myqueue.enqueue(queue, node.leftnode)
        if node.rightnode != None:
            myqueue.enqueue(queue, node.rightnode)
    return linkedlist.reverseList(valuesQueue)