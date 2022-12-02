def mdc(a, b):
        while a%b != 0:
            av = b
            b = a%b
            a = av
        return b
    
class Fraction:
    
    def __init__(self, cima, baixo ):
        self.num = cima
        self.den = baixo
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self, other):
        if self.den == other.den:
            nNun = (self.num * 1) + (other.num * 1)
            nDen = self.den
            
            
        else:
            nNun = (self.num * other.den) + (other.num * self.den)
            nDen = self.den * other.den
           
        return Fraction(nNun//mdc(nNun, nDen), nDen//mdc(nNun, nDen))
        
    def __sub__(self, other):
        if self.den == other.den:
            nNun = (self.num * 1) - (other.num * 1)
            nDen = self.den
        else:
            nNun = (self.num * other.den) - (other.num * self.den)
            nDen = self.den * other.den
            
        return Fraction(nNun//mdc(nNun, nDen), nDen//mdc(nNun, nDen))
            
    def __mul__(self, other):
        nNum = self.num * other.num
        nDen = self.den * other.den
        return Fraction(nNum//mdc(nNum, nDen), nDen//mdc(nNum, nDen))
    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Fraction(n//mdc(n, d), d//mdc(n, d))
    
    
##MAIN##
#Instanciando objetos
f = Fraction(3, 8)
f2 = Fraction(2, 8)

print(f)
print(f2)
#Operações com objetos
f3 = f + f2
print(f3)
f1 = f - f2
print(f1)
f4 = f3 * f1
print(f4)
f5 = Fraction(3, 4)/Fraction(3, 2)
print(f5)
    
