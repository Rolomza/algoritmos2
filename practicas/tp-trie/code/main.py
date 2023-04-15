from trie import *

trie1 = Trie()
trie2 = Trie()

insert(trie1,'ancho')
insert(trie1,'ancha')
insert(trie1,'antes')

insert(trie2,'ancho')
insert(trie2,'antes')
insert(trie2,'ancha')
# insert(trie2,'salco')



print(sameTries(trie1, trie2))
