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
        for node in node.children:
            if element[index] == node.key:
                insert_recursive(node, element, index + 1)
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
        for node in node.children:
            if element[index] == node.key:
                return search_recursive(node, element, index + 1)
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

def startsWith(T, p, n):
    trieWords = print_trie_words(T)
    patternWords = []
    for word in trieWords:
        if p == word[0:len(p)]:
            # Si no se especifica longitud
            if n == None:
                patternWords.append(word)
            # Si se especifica longitud
            if len(word) == n:
                patternWords.append(word)
    return patternWords

# EJERCICIO 5

def sameTries(T1,T2):
    T1List = print_trie_words(T1)
    T2List = print_trie_words(T2)
    if T1List == T2List:
        return True
    return False

# EJERCICIO 6

def has_inverted_words(T):
    trieWords = print_trie_words(T)
    for word in trieWords:
        reversedWord = "".join(reversed(word))
        if reversedWord in trieWords:
            return True
    return False

# EJERCICIO 7

def auto_complete(T,string):
    patternWords = startsWith(T,string,None)
    if len(patternWords) == 1:
        return patternWords[0].replace(string,'')
    else:
        return ''

# Funciones auxiliares

def print_trie_words(T):
	if T.root!=None:
		content=[]
		print_trie_recursive(T.root.children,content,"")
		return content
	else:
		return

def print_trie_recursive(children,wordsList,prefix):
	for node in children:
		if node.isEndOfWord:
			wordsList.append(prefix + node.key)
		if node.children!=None:
			print_trie_recursive(node.children, wordsList, prefix + node.key)
	return

    
    
    
    

    
    
    
    


        