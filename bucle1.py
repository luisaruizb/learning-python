'''
Bucle : loop, repetir una accion varias veces.
contadore ( cuenta e incrementa)
Acumuladores (Acumula valores )
contar valores es diferente de sumar valores
contador => c = c + k =>  k es una constante 
Incremento consecutivo y constante
cuantos datos hay?
'''
# Funcion Bucle para imprimir los numeros del 1 al 10 en pantalla

def list_num():
    i = 1
    while i <= 10:
        print(i)
        i+=1

    print("i: ",i)

def list_num2():
    i = 1
    status = True
    while status:
        if i <= 11:
            break
        print(i)
        i+=1
        
    print("i: ",i)

def list_num3():
    i = 1
    status = True
    while status:
        print(i)
        i+=1
        if i > 10 :
            status = False 
        
    print("i: ",i)

def list_num4():
    i = 1
    status = False
    while not status:
        print(i)
        i+=1
        if i > 10 :
            status = True 
        
    print("i: ",i)

#list_num()

#list_num2()

#list_num3()

list_num4()