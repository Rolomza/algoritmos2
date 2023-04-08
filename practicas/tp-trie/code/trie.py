class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

class TrieNode:
    def __init__(self) -> None:
        self.parent = None
        self.children = []
        self.key = None
        self.isEndOfWord = False

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
