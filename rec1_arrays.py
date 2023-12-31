# Escribe una funcion recursiva que tome una lista de numeros enteros y calcule la suma de todos los elementos de la lista. Puedes asumir que la lista no esta vacia.

numeros = [1,2,3,4,5]

# =========== EJEMPLO ITERATIVO =========== #
def suma_lista_iterativa(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print(suma_lista_iterativa(numeros))

# =========== EJEMPLO RECURSIVO =========== #
def suma_lista_recursiva(lista, indice = 0):
    if indice == len(lista) - 1:
        return lista[indice]
    else:
        return lista[indice] + suma_lista_recursiva(lista, indice + 1)
    
print(suma_lista_recursiva(numeros))
#Esta es una prueba
