from decouple import config
from googleapiclient.discovery import build
# import json

GOOGLE_API_KEY = config('GOOGLE_API_KEY') # Consiguen una aquí: https://developers.google.com/custom-search/v1/overview?hl=es-419#api_key
CX = config('CX') # Consiguen una aquí: https://cse.google.com/cse/create/new

'''
Tienen que colocar sus keys en un archivo .env en el 
mismo directorio que main.py con el siguiente formato:

GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxhrwZnSe88"
CX="xxxxxxxxxxx7346eb"
'''

def main():
    print("-"*50)
    print(" API Key:", GOOGLE_API_KEY)
    print(" CX     :", CX)
    print("-"*50, end="\n\n")

    # consulta = 'tallerista arte'
    consulta = input("Ingrese búsqueda: ")
    servicio = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    respuesta = servicio.cse().list(q=consulta, cx=CX).execute()

    # Este es para generar `test-sample.json`
    # with open('test-sample.json', 'w') as outfile:
        # if 'items' in respuesta:
            # json.dump(respuesta, outfile)

    # Y aquí un ejemplo de cómo leer los datos de la búsqueda
    # basándonos en el archivo `test-sample.json` como guía
    if 'items' in respuesta:
        for item in respuesta['items']:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}", end="\n\n")
    
    print('Fin de la búsqueda.')

if __name__ == "__main__":
    main()
