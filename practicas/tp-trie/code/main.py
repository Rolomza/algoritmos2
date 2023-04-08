from trie import *

myTrieTree = Trie()

print('primera palabra')
insert(myTrieTree,'sal')
print('Segunda palabra:')
insert(myTrieTree,'sol')
print('Tercera palabra:')
insert(myTrieTree,'santo')
print(myTrieTree.root.children[0].children[0].children[1].children[0].children[0].key)