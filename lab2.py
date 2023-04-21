import random

filas= input("Ingrese la cantidad de filas")
columnas= input("Ingrese la cantidad de columnas")

filas= 2
columas= 2

#se genera una matriz random
m1= [[random.randint(0.10) for j in range(columnas) for i in range(filas)]]
m2= [[random.randint(0.10) for j in range(columnas) for i in range(filas)]]

input(input(m1[i][j]*m2[i][j]))
print