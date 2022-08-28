n = int(input('digite um número: '))
print('Para {}!'.format(n))
for i in range(1, n):
    n = n * i
    
print(f'o resultado é {n}')


