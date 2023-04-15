from trie import *

trie1 = Trie()

insert(trie1,'ala')
insert(trie1,'alto')
insert(trie1,'alo')
insert(trie1,'alarmante')
insert(trie1,'alergia')


print(startsWith(trie1,'',0))
