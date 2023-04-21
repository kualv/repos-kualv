import random
import numpy as np

filas= input("Ingrese cantidad de filas")
columnas= input("Ingrese cantidad de columnas")

filas=2
columnas=2

j=columnas
i=filas

#se genera matrices random
m1= [[random.randint(0.5) for j in range(columnas) for i in range(filas)]]
m2= [[random.randint(0.5) for j in range(columnas) for i in range(filas)]]

suma= [[m1[i][j] + m2[i][j]]]
mr=suma

#se solicita la 3era matriz
filas= input("Ingrese cantidad de filas")
columnas= input("Ingrese cantidad de columnas")


m3= [[random.randint(0.5) for j in range(columnas) for i in range(filas)]]

resta= [[mr[i][j] - m3[i][j]]]



