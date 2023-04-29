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
        hash_table.insert(key,'')
    print(hash_table.table)
    print('')

#exercise1()

# Ejercicio 2: Implementacion de la estructura dictionary con sus metodos (insert,search y delete) ver archivo dictionary.py

# Ejercicio 3

'''
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al
método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves
61,62,63,64 y 65.

'''

def exercise3():
    print('Exercise 3')
    A = (math.sqrt(5)-1) / 2
    hash_function3 = lambda k: math.floor(1000*(k*A % 1))
    keys_set3 = [61,62,63,64,65]

    for key in keys_set3:
        print('h(%d):' %key,hash_function3(key))
    print('')

#exercise3()

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



# Ejercicio 5

'''
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
propuesta.
Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición
'''

def has_unique_elements(list):
    list_length = len(list)

    A = (math.sqrt(5)-1) / 2
    hash_function = lambda k: math.floor(list_length*(k*A % 1))
    hash_table = dictionary.Dictionary(list_length,hash_function)

    for i in range(len(list)):
        position = 'position: %d' %(i+1)
        hash_table.insert(list[i],position)
        if len(hash_table.table[i]) > 1:
            return 'Falso, la lista no tiene todos sus elementos unicos',hash_table.table[i]
    return True

# Ejercicio 6

'''
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter
(A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que
representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e
implementar una función de hash apropiada para los códigos postales argentinos.
'''

def postal_code_hash_function(code,m):
    # Codigo postal argentino 
    province_id = code[0]
    territorial_subdivision_id = code[1:5]
    city_block_side = code[5:]

    # Construyo el key numerico
    code_key = ord(province_id) * 10**4
    code_key += int(territorial_subdivision_id)

    exp = 2
    for i in range(len(city_block_side)):
        code_key += (ord(city_block_side[i]) - ord('A')) * 10**exp
        exp -= 1

    return code_key % m

# Ejercicio 7

'''
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
recuento de caracteres repetidos.
Por ejemplo, la cadena 'aabcccccaaa' se convertiría en 'a2blc5a3'.
Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
método debería devolver la cadena original.
Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z).
Justificar el coste en tiempo de la solución propuesta.
'''

def compress_string(s):
    if not s:
        return s  # Si la cadena está vacía, se devuelve tal cual

    compressed = []
    count = 1  # Contador para llevar el recuento de caracteres repetidos
    prev_char = s[0]  # Variable para almacenar el caracter previo inicialmente con el primer caracter de la cadena

    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            compressed.append(prev_char + str(count))
            prev_char = s[i]
            count = 1

    # Se agrega el último caracter y su contador a la lista comprimida después de finalizar el bucle
    compressed.append(prev_char + str(count))

    # Se crea la cadena comprimida uniendo los elementos de la lista comprimida
    compressed_str = ''.join(compressed)

    # Se compara la longitud de la cadena original y la cadena comprimida y se devuelve la cadena original si es más corta
    if len(compressed_str) >= len(s):
        return s
    else:
        return compressed_str
    
# Ejercicio 8

'''
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL.
Implementar esta estrategia de la forma más eficiente posible con un costo computacional
menor a O(K*L) (solución por fuerza bruta). Justificar el coste en tiempo de la solución propuesta.
'''

# Implementacion del algoritmo de Knuth-Morris-Prat para string matching.

def kmp_matcher(pattern, text):
    m = len(pattern)
    n = len(text)
    prefix = prefix_table(pattern, m)
    # Searching
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - m + 1
            j += 1
            i += 1
        else:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    return -1

def prefix_table(pattern, pattern_lenght):
    prefix = [0] * pattern_lenght
    j = 0
    for i in range(1, pattern_lenght):
        if pattern[i] == pattern[j]:
            prefix[i] = j + 1
            j += 1
        else:
            j = 0
    return prefix

# Complejidad temporal = O(m+n)

#print(kmp_matcher('cada','abracadabra'))

# Ejercicio 9

'''
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un
algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál
es la complejidad temporal del caso promedio del algoritmo propuesto?
'''
# S y T son sets, es decir no tienen elementos repetidos.

def is_subset(S,T):
    if len(S) > len(T):
        return False
    
    m = len(T)
    
    hash_function = lambda k: k % m
    hash_tableT = dictionary.Dictionary(m,hash_function)

    for num in T:
        hash_tableT.insert(num,num)

    print(hash_tableT.table)
    for s in S:
        if hash_tableT.search(s) != s:
            return False
    return True

# setT = [1,2,8,4,5]
# setS = [1,3]
# print(is_subset(setS,setT))
