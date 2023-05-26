import random

matriz_a = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
matriz_b = [[random.randint(11, 30) for _ in range(3)] for _ in range(3)]
matriz_c = [[random.randint(-10, -1) for _ in range(3)] for _ in range(3)]

resultado1 = []
for i in range(3):
    fila_resultado = []
    for j in range(3):
        suma = matriz_a[i][j] + matriz_b[i][j]
        producto = 0
        for k in range(3):
            producto += (suma*matriz_c[k][j])
        fila_resultado.append(producto)
    resultado1.append(fila_resultado)

resultado2 = []
for i in range(3):
    fila_resultado = []
    for j in range(3):
        producto_ac = 0
        producto_bc = 0
        for k in range(3):
            producto_ac += (matriz_a[i][k]*matriz_c[k][j])
            producto_bc += (matriz_b[i][k]*matriz_c[k][j])
        fila_resultado.append(producto_ac + producto_bc)
    resultado2.append(fila_resultado)

son_iguales = resultado1 == resultado2

print("¿(A+B)·C = A·C + B·C?")
print(son_iguales)

