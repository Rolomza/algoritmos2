class Dictionary:
    def __init__(self,slots,hash_function):
        # slots equivale a 'm' en la teoria
        self.slots = slots
        self.hash_function = hash_function
        self.table = [[] for _ in range(slots)]

    def insert(self,key,value):
        table_slot = self.hash_function(key)
        self.table[table_slot].append((key,value))
        return self.table
    
    def search(self,key):
        table_slot = self.hash_function(key)
        for tuple in self.table[table_slot]:
            if tuple[0] == key:
                return tuple[1]
        return

    def delete(self,key):
        table_slot = self.hash_function(key)
        for tuple in self.table[table_slot]:
            if tuple[0] == key:
                self.table[table_slot].remove(tuple)

