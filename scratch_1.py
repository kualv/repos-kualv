# imprimeFib: int -> None
# imprime los n-ésimos primeros números de la serie de
# Fibonacci

def imprimeFib(n):
    a = 1
    b = 1
    if n == 1:
        print("0")
    elif n == 2:
        print("1", "0")
    else:
        print("0")
        print(a)
        print(b)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)


imprimeFib(50)
#sumaArr(a,b): list list -> list
#entrega un nuevo arreglo de tamaño n+1 que es el resutado
#de la suma de a y b
#ej: sean los arreglos a = [9,8,7,6] y b = [8,7,6,
#5], ambos de tamaño 4, sumarArr(a, b) entrega un nuevo
#arreglo [1,8,6,4,1] de tamaño 5
