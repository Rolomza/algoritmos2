class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

class TrieNode:
    def __init__(self) -> None:
        self.parent = None
        self.children = []
        self.key = None
        self.isEndOfWord = False

# EJERCICIO 1

def insert(T,element):
    if element == '':
        return
    index = 0
    insert_recursive(T.root, element, index)

def insert_recursive(node, element, index):
    if index > len(element) - 1:
        return
    parent = node
    if node.children != []:
        for child in node.children:
            if element[index] == child.key:
                insert_recursive(child, element, index + 1)
                return
    
    while index <= len(element) - 1:
        newNode = TrieNode()
        newNode.key = element[index]
        newNode.parent = parent
        parent.children.append(newNode)
        parent = newNode
        index += 1

    newNode.isEndOfWord = True
    return

def search(T,element):
    if element == '':
        return False
    index = 0
    return search_recursive(T.root, element, index)

def search_recursive(node, element, index):
    if index > len(element) - 1:
        if node.isEndOfWord == True:
            return True
        else:
            return False

    if node.children != []:
        for child in node.children:
            if element[index] == child.key:
                #print('Letra hallada:', element[index])
                return search_recursive(child, element, index + 1)
    return False

# EJERCICIO 3

def delete(T,element):
  if search(T,element) == False:
    return False
    
  node = T.root
  for ch in element:  ### Recorre cada letra del elemento (palabra) ###
    index = traverse_list(node.children,ch)
    if index == None:  ### No se encuentra la letra en la lista ###
      return False
    else:  ### Se encuentra la letra en la lista ###
      node = node.children[index]  ### Sigue al proximo nodo ###
  if node.children != []:  ### Si la palabra a eliminar es parte de una palabra mas larga (hola,holanda) ###
    node.isEndOfWord == False
    return True
  else:
    delete_node(T,node)
    return True

def delete_node(T,node):
  temp = node 
  node = node.parent 
  node.children.remove(temp)  
  if node.isEndOfWord == True or node == T.root or len(node.children) > 0:
    return True
  else:
    delete_node(T,node)

def traverse_list(list, ch):
    for index, i in enumerate(list):
      if i.key == ch:
         return index
    return None

# EJERCICIO 4

def starts_with(T, p, n):
    def find_words(current, words, current_str, max_length):
        # Recursive function for searching the word
        # When the length is reached
        if len(current_str) == max_length:
            if current.isEndOfWord:
                # Adds the word and quits recursion
                words.append(current_str)
            return
        # For every child
        for child in current.children:
            find_words(child, words, current_str + child.key, max_length)
    # Checks there if exists any word starting with char
    for child in T.root.children:
        if child.key == p:
            break
    else:
        return
    
    words = []
    find_words(child, words, child.key, n)
    return words

# EJERCICIO 5



