'''
API Aplication Programming Interface
Nasa API: Get comets 
API_KEY_NASA: Qtzb35JEnpb6CnDaa8j4hjnNnVb1nnKHwc6wsTwo
Developer: Luisa Ruiz
Date: 24012024
Script description: Get data from NASA API about comets
'''

import requests 


def get_comet_data(api_key):
    print("COMET INFORMATION")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        #Realizar la solicitud a la API 
        response = requests.get(url) #=> Valida si se presenta algun error en la peticion 
        # convertir la respuesta a formato JSON (JS object notation)
        datos = response.json()

        print(f"comet name: {datos['name']}")
        print(f"Absolute Magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max: {datos['estimated_diameter']['kilometers']["estimated_diameter_max"]}")


    except requests.exceptions.requestsException as e:



        response.raise_for_status()




api_key_nasa = 'Qtzb35JEnpb6CnDaa8j4hjnNnVb1nnKHwc6wsTwo'
get_comet_data(api_key_nasa)






