from trie import *

myTrieTree = Trie()

insert(myTrieTree,'ala')
insert(myTrieTree,'alambre')
insert(myTrieTree,'sal')
insert(myTrieTree,'espada')
insert(myTrieTree,'estado')

print(myTrieTree.root.children[2].key)
print(myTrieTree.root.children[2].children[0].children)
print(delete(myTrieTree,'estado'))
print(myTrieTree.root.children[2].key)
print(myTrieTree.root.children[2].children[0].children)