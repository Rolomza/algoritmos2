class Trie:
    root = None

class trieNode:
    parent = None
    children = []
    key = None
    isEndOfWord = False

def insert(T, element):
    if T.root == None:
        T.root = trieNode()
        T.root.key = '*'

    if element == '':
        return 

    insertR(T.root, element, 0)
    
def insertR(node, element, i):
    parent = node

    newNode = trieNode()
    newNode.key = element[i]
    newNode.parent = parent
    parent.children.append(newNode)

    if i == len(element) - 1:
        newNode.isEndOfWord = True
        return
    else:
        i = i + 1

    insertR(newNode, element, i)
    

    



    