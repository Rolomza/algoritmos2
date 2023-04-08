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
    # print('-- Comienzo de funcion --')
    # print('index:', index, 'element[index]:', element[index], 'parent:', parent.key)
    # Busco en el children del actual nodo si existe el primer caracter de mi elemento
    if node.children != []:
        for child in node.children:
            if element[index] == child.key:
                print('Llamado recursivo')
                insert_recursive(child, element, index + 1)
                return
    # print('-- Antes de ingresar al while --')
    # print('index:', index, 'element[index]:', element[index], 'parent:', parent.key)
    
    while index <= len(element) - 1:
        # print('-- Crear e insertar nuevo nodo no existente: --')
        # print('index:',index,'element[index]:', element[index], 'parent:', parent.key)
        newNode = TrieNode()
        newNode.key = element[index]
        newNode.parent = parent
        parent.children.append(newNode)
        parent = newNode
        index += 1

    newNode.isEndOfWord = True
    return




