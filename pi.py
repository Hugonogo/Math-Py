pi = 0
for i in range(0, 2):
    pi = pi + 4 * ((-1)**i) / (2*i + 1)
print('{:.6f}'.format(pi))
