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
    S = set()
    for num in A:
        if n - num in S:
            return True
        S.add(num)
    return False

print(contieneSuma([1,2,3],5))