from decouple import config
from googleapiclient.discovery import build

class Tallerista:
    def __init__(self, nombre, linkedin, foto_perfil) -> None:
        self.nombre = nombre
        self.linkedin = linkedin
        self.foto_perfil = foto_perfil

GOOGLE_API_KEY = config('GOOGLE_API_KEY')
CX = config('CX')

def google_custom_search(consulta):
    servicio = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    respuesta_api = servicio.cse().list(q=consulta, cx=CX).execute()
    respuesta = []

    if 'items' in respuesta_api:
        for item in respuesta_api['items']:
            try:
                item['pagemap']['metatags'][0]['og:image']
            except:
                continue

            tallerista = Tallerista(
                item['title'],
                item['link'],
                item['pagemap']['metatags'][0]['og:image']
            )

            respuesta.append({
                'titulo': tallerista.nombre,
                'enlace': tallerista.linkedin,
                'foto_perfil': tallerista.foto_perfil
            })
            
    return respuesta
