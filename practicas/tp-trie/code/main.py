from trie import *

myTrieTree = Trie()

#print('primera palabra')
insert(myTrieTree,'sal')
#print('Segunda palabra:')
insert(myTrieTree,'sol')
#print('Tercera palabra:')
insert(myTrieTree,'santo')
insert(myTrieTree,'solana')
insert(myTrieTree,'pan')
insert(myTrieTree,'palco')

#print(myTrieTree.root.children[1].children[0].children[1].key)

print(search(myTrieTree, 'palco'))