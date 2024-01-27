'''
Bucle que genere un N cantida de numeros aleatorios.
El usuario debe digital la cantida de numeros enteros a generar

'''
import os
import random

def numbers_generator(cant):
    i= 1
    pares= 0
    impares = 0
    positivos = 0
    negativos =  0
    sum_pos = 0 
    sum_neg = 0

    while i <= cant:
        num = random.randint(-100,100)
        print(num)

        if num % 2 == 0:
            pares = pares + 1
        else:
            impares += 1

        if num > 0:
            positivos = positivos + 1
            sum_pos = sum_pos + num
        else:
            negativos += 1
            sum_neg += 1

        i += 1

            
    print(f"Total numeros generados: {cant}")
    print(f"Total pares generados: {pares}")
    print(f"Total impares  generados: {impares}")
    print(f"Total positivos  generados: {positivos}")
    print(f"Total negativos  generados: {negativos}")




        

cant_num = int(input("Qué cantidad de numeros deseas generar: "))
numbers_generator(cant_num)