class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def add(L,element):
  newNode = Node()
  newNode.value = element
  newNode.nextNode = L.head
  L.head = newNode
  return


def search(L,element):
  currentNode = L.head
  currentPos = 0
  
  while currentNode != None:
    
    if currentNode.value == element:
      return currentPos

    currentNode = currentNode.nextNode
    currentPos += 1

  return None


def insert(L,element,position):
  currentNode = L.head
  currentPos = 0

  if position == 0:
    add(L,element)
    return currentPos
  
  while currentNode != None and currentPos < position - 1:
    currentNode = currentNode.nextNode
    currentPos += 1

  if currentNode != None:
    newNode = Node()
    newNode.value = element
    newNode.nextNode = currentNode.nextNode
    currentNode.nextNode = newNode
    return currentPos + 1

def delete(L,element):
  currentNode = L.head
  prevNode = None
  currentPos = 0

  while currentNode != None:
    if currentNode.value == element:
      if currentPos == 0:
        L.head = currentNode.nextNode
      else:
        prevNode.nextNode = currentNode.nextNode
      return currentPos
      
    prevNode = currentNode
    currentNode = currentNode.nextNode
    currentPos += 1

  return None
  
def length(L):
  totalElements = 0
  currentNode = L.head
  while currentNode != None:
    totalElements += 1
    currentNode = currentNode.nextNode
  return totalElements

def access(L,position):
  currentNode = L.head
  currentPos = 0
  while currentNode != None:
    if currentPos == position:
      return currentNode.value
    currentNode = currentNode.nextNode
    currentPos += 1
  return None

def getNode(L,position):
  currentNode = L.head
  currentPos = 0
  while currentNode != None:
    if currentPos == position:
      return currentNode
    currentNode = currentNode.nextNode
    currentPos += 1
  return None
  
def update(L,element,position):
  currentNode = L.head
  currentPos = 0

  while currentNode != None:
    if currentPos == position:
      currentNode.value = element
      return currentPos
      
    currentNode = currentNode.nextNode
    currentPos += 1

  return None

def reverseList(list):
  newList = LinkedList
  current = list.head
  while current != None:
      add(newList,current.value)
      current = current.nextNode
  return newList

# Implementar funcion Move

def move(L, pos_origin, pos_dest):
    # Catching Errors
    len = length(L)
    if pos_origin < 0 or pos_origin > len:
        return
    if pos_dest < 0 or pos_dest > len:
        return
    if pos_dest == pos_origin:
        return

    nodeDisplaced = getNode(L, pos_dest)
    nodeBeforeDisplaced = getNode(L, pos_dest - 1)
    nodeToMove = getNode(L, pos_origin)
    nodeBeforeMoved = getNode(L, pos_origin - 1)
    # Left To Right
    if pos_origin < pos_dest:
        if pos_origin == 0:
            L.head = nodeToMove.nextNode
        else:
            nodeBeforeMoved.nextNode = nodeToMove.nextNode
        nodeToMove.nextNode = nodeDisplaced.nextNode
        nodeDisplaced.nextNode = nodeToMove
    # Right To Left
    else:
        if pos_origin == length(L) - 1:
            nodeBeforeMoved.nextNode = None
        else:
            nodeBeforeMoved.nextNode = nodeToMove.nextNode
        nodeToMove.nextNode = nodeDisplaced
        if pos_dest != 0:
            nodeBeforeDisplaced.nextNode = nodeToMove
        else:
            L.head = nodeToMove
    return pos_origin

  
def imprimirLista(lista):
  currentNode = lista.head
  while currentNode != None:
    if(currentNode.nextNode != None):
      print('|',currentNode.value,'|->', end=" ")
    else:
      print('|',currentNode.value,'|-> None')
    currentNode = currentNode.nextNode
  print('')