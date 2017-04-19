'''x = "1234567890"
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

while True:
    y = input("ingrese")
    if y in x:
        lista.remove(lista[int(y)])
        break
    else:
        print("Dar invalido")
print(lista)
'''
'''
while True:
    x = input("ingrese")
    if isinstance(x,(int)):
       x = int(x)
       print(x)
    else:
        x = int(x)
        x = x+1
        print(x)
'''
'''
x = input("ingre")
x = x.upper()
print(x)
'''