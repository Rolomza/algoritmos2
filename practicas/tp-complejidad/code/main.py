# Ejercicio 4

miLista = [5,2,4,1,3,6,7,8,9,10]

def ordenarLista(lista):
    # Copio y ordeno la lista
    nuevaLista = lista.copy()
    nuevaLista.sort()
    # Determino indice y valor del pivot
    indexPivot = (len(nuevaLista) - 1) // 2
    pivot = nuevaLista[indexPivot]
    # Variable auxiliar para contabilizar elementos a dejar por debajo
    cantidadElementosMenores = pivot // 2

    i = indexPivot
    # Una vez ordenada la lista se recorre desde el comienzo hasta el pivot
    for j in range(0,indexPivot):
        # Como la lista se ordeno antes de recorrerla, una vez iteremos la mitad de elementos menores que el pivot
        # las iteraciones por encima de esa cantidad pasaran esos valores al otro lado del pivot en la lista
        cantidadElementosMenores = cantidadElementosMenores - 1
        if cantidadElementosMenores < 0:
            i = i + 1
            # Swap de valores de la lista por debajo y por encima del pivote
            nuevaLista[j], nuevaLista[i] = nuevaLista[i], nuevaLista[j]
    return nuevaLista

print(miLista)
print(ordenarLista(miLista))

# Ejercicio 5

def contieneSuma(A,n):
    return

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                print('entro aca')
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [1, 1, 1, 1, 1]

# insertionSort(arr)
# print(arr)

# for i in range(len(arr)):
#     print ("% d" % arr[i])
