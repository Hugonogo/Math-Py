pi = 0
for i in range(0, 1000000):
    pi = pi + 4 * ((-1)**i) / (2*i + 1)
print('{:.6f}'.format(pi))
