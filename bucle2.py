def cajero():
    my_clave_ban = '2024'

    cont_attemps = 1
    status = True

    while status:
        clave = input("Digita tu clave: ")
        if my_clave_ban == clave :
            print("has ingresado a tu cuenta")
            print(f"intento satisfactorio: {cont_attemps}")
            status = False
        else:
            if cont_attemps < 3 :
                print(f"intento {cont_attemps}: clave incorrecta, intente nuevamente")
                cont_attemps +=1

            else : 
                print(f"intento {cont_attemps}: clave incorrecta, intenta nuevamente")
                cont_attemps += 1

            if cont_attemps > 3 :
                print ("se han agotados los intentos permitidos")
                break

cajero()
