class Dictionary:
    def __init__(self,slots,hash_function):
        # slots equivale a 'm' en la teoria
        self.slots = slots
        self.hash_function = hash_function
        self.table = [None for _ in range(slots)]

    def insert(self,key):
        i = 0
        while i < self.slots:
            table_slot = self.hash_function(key,i)
            if self.table[table_slot] == None:
                self.table[table_slot] = key
                return self.table
            else:
                i += 1
        return self.table
    
    # def search(self,key):
    #     table_slot = self.hash_function(key)
    #     for tuple in self.table[table_slot]:
    #         if tuple[0] == key:
    #             return tuple[1]
    #     return

    # def delete(self,key):
    #     table_slot = self.hash_function(key)
    #     for tuple in self.table[table_slot]:
    #         if tuple[0] == key:
    #             self.table[table_slot].remove(tuple)

# Ejercicio 10

keys_list = [10,22,31,4,15,28,17,88,59]

def hashing_linear_probing(keys_list,m):
    hash_function = lambda k,i: (k + i) % m
    hash_table = Dictionary(m,hash_function)

    for key in keys_list:
        hash_table.insert(key)
    print('Linear probing hashing:',hash_table.table)

#hashing_linear_probing(keys_list,11)
# Resultado = [22, 88, None, None, 4, 15, 28, 17, 59, 31, 10]

def hashing_cuadratic_probing(keys_list,m):
    c1,c2 = 1,3
    hash_function = lambda k,i: (k + (c1*i) + (c2*(i**2))) % m
    hash_table = Dictionary(m,hash_function)

    for key in keys_list:
        hash_table.insert(key)
    print('Cuadratic probing hashing:',hash_table.table)

#hashing_cuadratic_probing(keys_list,11)
# Resultado = [22, None, 88, 17, 4, None, 28, 59, 15, 31, 10]

def double_hashing(keys_list,m):
    hk1 = lambda k: k
    hk2 = lambda k: 1 + (k % (m-1))
    hash_function = lambda k,i: (hk1(k) + i*hk2(k)) % m
    hash_table = Dictionary(m,hash_function)

    for key in keys_list:
        hash_table.insert(key)
    print('Double hashing:',hash_table.table)

#double_hashing(keys_list,11)
# Resultado = [22, None, 59, 17, 4, 15, 28, 88, None, 31, 10]

def ejercicio12():
    keys_list = [12,18,13,2,3,23,5,15]
    hashing_linear_probing(keys_list,10)

#ejercicio12()

def ejercicio13():
    keys_list = [46,34,42,23,52,33]
    hashing_linear_probing(keys_list,10)

#ejercicio13()

