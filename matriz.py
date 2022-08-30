#Algumas operações com matrizes 
import numpy as np
m1 = np.array([10, 12, 5, 6, 11, 4, 6, 0, 9, 17, 14, 1], dtype = 'int64').reshape(4, -1) #conjuntos de elementos de um mesmo tipo
m1.shape = (3, 4) #Forma do tensor, utilizado para fazer matriz
m2 =np.array([12, 15, 1, 5, 7, 19, 0, 6, 8, 3, 9, 20]).reshape(4, -1)
m2.shape = (3, 4)
m3 = 0
m4 = 0
m5 = 0

print("Matriz m1")
print(m1)

print("="*15)

print("Matriz m2")
print(m2)

print("="*15)

print("Matriz m3 = m1 + m2")
m3 = m1 + m2
print(m3)

print("="*15)

print("Matriz m4 = m1 - m2")
m4 = m1 - m2
print(m4)

print("="*15)

print("Matriz m5 = m1 . x")
x = int(input("Digite um número: "))
m5 = m1 * x
print(m5)
