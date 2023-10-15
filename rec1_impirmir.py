# ========== Iprimir los numeros del 1 al 10 ==========

# EJEMPLO ITERATIVO
for i in range(1, 11):
    print(i)    
     
# EJEMPLO RECURSIVO
def mostrar_recursivo(n):
    if n > 0:
        mostrar_recursivo(n - 1)  
        print(n)

mostrar_recursivo(10)

# ========= Imprimir los numeros desde 10 al 1 ==========

# EJEMPLO ITERATIVO
for i in range(10, 0, -1):
    print(i)
    
#EJEMPLO RECURSIVO
def mostrar_numeros_2(n):
    if n > 0:
        print(n)
        mostrar_numeros_2(n - 1)
        
mostrar_numeros_2(10)