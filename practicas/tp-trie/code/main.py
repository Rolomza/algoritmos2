from trie import *

myTrieTree = Trie()

insert(myTrieTree,'ala')
insert(myTrieTree,'aso')
insert(myTrieTree,'ama')
insert(myTrieTree,'alambre')
insert(myTrieTree,'sal')
insert(myTrieTree,'espada')
insert(myTrieTree,'estado')

print(starts_with(myTrieTree,'e',6))