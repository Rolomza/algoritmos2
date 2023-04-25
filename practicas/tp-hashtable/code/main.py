import dictionary
import math

# Ejercicio 1

'''
Ejemplificar que pasa cuando insertamos las llaves 5, 28, 19, 15, 20, 33, 12, 17, 10 en un HashTable
con la colisión resulta por el método de chaining. Permita que la tabla tenga 9 slots y la función de
hash: H (k) = k mod 9
'''

def exercise1():
    print('Exercise 1')
    hash_function1 = lambda k : k % 9
    hash_table = dictionary.Dictionary(9,hash_function1)
    keys_set = [5,28,19,15,20,33,12,17,10]
    for key in keys_set:
        hash_table.insert(key,'data')
    print(hash_table.table)
    print('')

exercise1()

# Ejercicio 2: Implementacion de la estructura dictionary con sus metodos (insert,search y delete) ver archivo dictionary.py

# Ejercicio 3

'''
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al
método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves
61,62,63,64 y 65.

'''

def exercise2():
    print('Exercise 2')
    A = (math.sqrt(5)-1) / 2
    hash_function3 = lambda k: math.floor(1000*(k*A % 1))
    keys_set3 = [61,62,63,64,65]

    for key in keys_set3:
        print('h(%d):' %key,hash_function3(key))
    print('')

exercise2()

# Ejercicio 4

'''
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente
proposición: dado dos strings s1...sk y p1...pk, se quiere encontrar si los caracteres de p1...pk
corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = 'hola' , P = 'ahlo'
Salida: True, ya que P es una permutación de S
Ejemplo 2:
Entrada: S = 'hola' , P = 'ahdo'
Salida: Falso, ya que P tiene al carácter 'd' que no se encuentra en S por lo que no es una
permutación de S

'''

def is_permutation(string1,string2):
    if len(string1) != len(string2) or string1 == string2:
        return False
    
    str_length = len(string1)
    A = (math.sqrt(5)-1) / 2
    hash_function = lambda k: math.floor(str_length*(k*A % 1))
    hash_table = dictionary.Dictionary(str_length,hash_function)

    for char in string1:
        hash_table.insert(ord(char),char)
    
    for char in string2:
        if hash_table.search(ord(char)) == None:
            return False
    
    return True




    
    



