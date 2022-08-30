def fah(a):
    f = ((9*a)/5) + 32
    return f


C = int(input("insira uma Temperatura em C°: "))

print(f'{C} C° ===> {fah(C):,.2f} F°')

