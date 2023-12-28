# ========== 1.Sumar los numeros naturales hasta N (se lo damos nosotros) de forma recursiva. ========== #

#EJEMPLO CON FOR:
def suma_iterativa(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
print(suma_iterativa(5))

#EJEMPLO RECURSIVO
def suma_recursiva(n):
    if n == 0:  #este es mi caso base.
        return 0
    else:
        return n + suma_recursiva(n - 1)
    
print(suma_recursiva(5))

# ========== 2.Factorial de un numero. ========== # 

#EJEMPLO CON FOR:
def factorial_iterativo(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(factorial_iterativo(5))

#EJEMPLO RECURSIVO
def factorial_recurivo(n):
    if n == 1:
        return 1
    else:
        return  factorial_recurivo(n - 1) * n
    
print(factorial_recurivo(5))
#ESta es una prueba