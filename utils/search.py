from decouple import config
from googleapiclient.discovery import build

GOOGLE_API_KEY = config('GOOGLE_API_KEY')
CX = config('CX')

def google_custom_search(consulta):
    servicio = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    respuesta_api = servicio.cse().list(q=consulta, cx=CX).execute()
    respuesta = []
    if 'items' in respuesta_api:
        for item in respuesta_api['items']:
            titulo = item['title']
            enlace = item['link']
            try:
                foto_perfil = item['pagemap']['metatags'][0]['og:image']
            except:
                continue
            respuesta.append({
                'titulo': titulo,
                'enlace': enlace,
                'foto_perfil': foto_perfil
            })
    return respuesta
