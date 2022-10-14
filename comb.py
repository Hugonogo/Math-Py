#Combinação simples em python

def fatorial(numero):
    if(numero == 0):
        return 1
    else:
        for i in range(1, numero):
            numero = numero * i
        
        return numero

def comb(n, k):
    nmk = n - k
    n = fatorial(n)
    k = fatorial(k)
    nmk = fatorial(nmk)
    
    return n / (k * nmk)


n = int(input("--> "))
k = int(input("--> "))

print(f"C{n}, {k} = {comb(n, k)}")
