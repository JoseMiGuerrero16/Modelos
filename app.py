from decouple import config
from googleapiclient.discovery import build
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/buscar', methods=['POST'])
def buscar_datos():
    data = request.get_json()
    consulta = data.get('consulta')
    resultados = google_custom_search(consulta)
    return jsonify(resultados)

GOOGLE_API_KEY = config('GOOGLE_API_KEY') # Consiguen una aquí: https://developers.google.com/custom-search/v1/overview?hl=es-419#api_key
CX = config('CX') # Consiguen una aquí: https://cse.google.com/cse/create/new

def google_custom_search(consulta):
    servicio = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    respuesta_api = servicio.cse().list(q=consulta, cx=CX).execute()
    respuesta = []
    if 'items' in respuesta_api:
        for item in respuesta_api['items']:
            titulo = item['title']
            link = item['link']
            try:
                pfp = item['pagemap']['metatags'][0]['og:image']
            except:
                continue
            respuesta.append({'title': titulo, 'link': link, 'profile_picture': pfp})
    return respuesta

if __name__ == "__main__":
    app.run(debug=True)
