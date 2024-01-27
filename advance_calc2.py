'''
Calculadora que reciba 2 numerosy realice 
la operación aritmetica que el usuario desee.
puede escoger entre sumar, restar, mult o dividir
'''

import os 

os.system("clear")


def calculator(x, y, z):
    if z == '1' : 
        return z == x + y
    elif z == '2' :
        return z == x - y 
    elif z == '3' :
        return x * y
    elif z == '4' :
        return x / y
    else :
        return 'fail, invalid option'
     else :
        return 'no es posible dividir entre 0'

    

n1 = float(input ("ingrese primer valor: "))
n2 = float(input ("ingrese segundo valor: "))

print ("MENU CALCULADORA")
print ("[1]. Sumar")
print ("[2]. restar")
print ("[3]. Multiplicar")
print ("[4]. Dividir")
print ("[5]. Todas")

opc = input("digite una opcion del menu")

ans = calculator(n1, n2, opc)
print("resultado:", ans)