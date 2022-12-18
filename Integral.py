def func(x): 
	return 4 - x**2
 
a = 0
b = 2 

ret = int(input("Digite a Quantidade de retângulos: ")) 

base = (float(b - a) / ret) 
p = 0 
 
x = float(a)
altura = 0  
area = 0
while p < ret : 
	
	f = func(x) 
	if p == 0 : 
		altura = a + base / 2

	altura = f + base / 2
		
 
	area = area + (base * altura)
	x = x + base
	p = p + 1 
	 

print ('Valor da integral no intervalo indo de '+str(a)+' a '+str(b)+': '+str(area))
 