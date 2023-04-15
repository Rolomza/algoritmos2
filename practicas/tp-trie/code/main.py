from trie import *

trie1 = Trie()

insert(trie1,'alto')
insert(trie1,'altopico')
insert(trie1,'altonto')
insert(trie1,'otlas')


print(auto_complete(trie1,'ot'))
