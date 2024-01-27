#script que genere el lanzamiento de dos dados (1-6) 
#y que muestre en pantalla el mensaje ganador 
#cuando genere un para de seis de lo contrario el mensaje dira sigue intentando

#Importo biblioteca para generar numeros aleatorios enteros
from random import randint

#lanzar y generar los valores de los dos dados
def dices():        
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

d = dices()
d1 = d[0]
d1 = d[1]


print("dices:",d)
print ("dice 1:", d[0])
print ("dice 1:", d[1])


