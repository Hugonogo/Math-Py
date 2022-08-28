n1 = 0
n2 = 1
soma = 0
num_de_sequencia = int(input("Insira quantos números a sequência deve ter: "))
print("sequência de Fibonacci: ", end = " ")
for i in range(0, num_de_sequencia):
   print(soma , end= " ")
   n1 = n2
   n2 = soma
   soma = n2 + n1
    
 