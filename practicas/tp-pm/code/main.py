# PARTE 1

# Ejercicio 1
'''
Implementar la función que responde a la siguiente especificación.
def existChar(String, c):
	Descripción: Confirma la existencia de un carácter específico en una cadena.
    Entrada: String con la cadena en la cual buscar el carácter, carácter a buscar en la cadena.
    Salida: Retorna True si el carácter se encuentra en la cadena, o False en caso contrario
'''

def exist_char(string,char):
    for element in string:
        if element == char:
            return True
    return False

# Ejercicio 2

'''
Implementar una función que detecte si una cadena es un Palíndromo. La implementación debe responder a la siguiente especificación:

def isPalindrome(String):
	Descripción: Determina si la cadena es un palíndromo
    Entrada: String con la cadena a evaluar.
    Salida: Retorna True si la cadena es palíndromo, o False en caso contrario

La función es Palíndromo que devuelve True si una cadena es Palindromo y Falso en caso contrario.
Nota: Una cadena es un palíndromo si se lee igual en ambos sentidos ej. anitalavalatina, radar.
'''

def is_palindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True



# Ejercicio 3
'''
Implementar la función que responde a la siguiente especificación.
def mostRepeatedChar(String):
	Descripción: Encuentra el carácter que más se repite en una cadena.
    Entrada: String con la cadena a ser evaluada.
    Salida: Retorna el carácter que más se repite. En caso que haya más de un carácter con mayor ocurrencia devuelve el primero de ellos.
'''

def most_repeated_char(string):
    char_repetition = {}
    for char in string:
        if char not in char_repetition:
            char_repetition[char] = 0
        if char in char_repetition:
            char_repetition[char] += 1
    
    max_repetition_number = sorted(list(char_repetition.values()),reverse=True)[0]

    for char, value in char_repetition.items():
        if value == max_repetition_number:
            return char


# Ejericio 4

'''
Implementar la función que dado un String S devuelve la longitud de la isla de mayor tamaño. Una isla
es una secuencia consecutiva de un mismo carácter dentro de S. Por ejemplo S =
“cdaaaaaasssbbb” su mayor isla es de tamaño 6 (aaaaaa) y además tiene dos islas de tamaño 3
(sss, bbb) el resto de las islas en s son de tamaño 1.
def getBiggestIslandLen(String):
    Descripción: Determina el tamaño de la isla de mayor tamaño en una
    cadena.
    Entrada: String con la cadena a ser evaluada.
    Salida: Retorna un entero con la dimensión de la isla más grande
    dentro de la cadena.
'''


