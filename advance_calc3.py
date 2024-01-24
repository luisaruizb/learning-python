import os 

os.system("clear")

def todasop(x,y):
    print("El resultado de la suma es: =" , x + y)
    print("El resultado de la resta es: = " , x - y)
    print("El resultado de la multiplicación = " , x * y)
    if y != 0 :
        print("El resultado de la división es: = " , x / y)
    else:
        print("No es divisible")


def calculator(x, y, z):
    if z == '1' : 
        return z == x + y
    elif z == '2' :
        return z == x - y 
    elif z == '3' :
        return x * y
    elif z == '4' :
        if y != 0 :
            return x / y
        else:
            return 'No es posible dividir entre 0'
    elif z == '5' :
        todasop(x,y)

    

n1 = float(input ("ingrese primer valor: "))
n2 = float(input ("ingrese segundo valor: "))

print ("MENU CALCULADORA")
print ("[1]. Sumar")
print ("[2]. restar")
print ("[3]. Multiplicar")
print ("[4]. Dividir")
print ("[5]. Todas")

opc = input("Digite una opcion del menu: ")

ans = calculator(n1, n2, opc)

if ans != None:
    print("resultado: ", ans)