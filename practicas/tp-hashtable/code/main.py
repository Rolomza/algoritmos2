# Acompañamiento de teoria

class Dictionary:
    def __init__(self,slots):
        # slots equivale a 'm' en la teoria
        self.slots = slots
        self.table = [[] for _ in range(slots)]

    def hash_function(self,k):
        return k % 5

    def insert(self,key,value):
        self.table[self.hash_function(key)].append((key,value))
        return self.table
    
    def search(self,key):
        table_slot = self.hash_function(key)
        for tuple in self.table[table_slot]:
            if tuple[0] == key:
                return tuple[1]

    def delete(self,key):
        table_slot = self.hash_function(key)
        for tuple in self.table[table_slot]:
            if tuple[0] == key:
                self.table[table_slot].remove(tuple)


dict1 = Dictionary(6)
print('Dictionary original')
print(dict1.table)
print('Dictionary con insert')
dict1.insert(0,100)
dict1.insert(3,20)
dict1.insert(8,99)
print(dict1.table)
dict1.delete(8)
print(dict1.table)
