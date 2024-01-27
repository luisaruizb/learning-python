import requests
import os

os.system('clear')

def get_comets():
    global count
    print("Información del cometa")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
   
    try:
        #request to API 
        response = requests.get(url)
        response.raise_for_status()

   
        data = response.json()
        #print(data)
        count = 0

        total = int(input("Cantidad a mostrar: "))

        for comet in data ["bodies"]:
            if comet ["isPlanet"] == true:
        
                print("English name: ", comet["englishName"])
                print("Moons: ", comet["moons"])
                print("Gravity: ", comet["gravity"])
                print("Is planet?: ", comet["isPlanet"])
                print("\n")

                count = count + 1
            if count == total:
                break
        print(count)

    except requests.exceptions.requestsException as e:
        print(f"API error:{e}")

#llamado de la funcion 
get_comets()
