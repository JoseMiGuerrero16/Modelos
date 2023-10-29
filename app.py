from flask import Flask, render_template, request, jsonify
from src.utils.search import google_custom_search

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

if __name__ == "__main__":
    app.run(debug=True)
