import random

def Mostrar_Matriz(matriz):
    for fila in matriz:
        print(fila)
    
matriz1=[[2,3,4],[3,4,5],[4,5,2]]
matriz2=[[4,3,2],[5,4,3],[2,5,4]]
matriz=[]
for i in range(len(matriz1)):
    auxl=[]
    for j in range(len(matriz2[0])):
        aux=0
        for k in range(len(matriz1[0])):
            aux-=matriz1[i][k]*matriz2[k][j]
        auxl.append(aux)
    matriz.append(auxl)
print(matriz1)
print(matriz2)
print(matriz)




