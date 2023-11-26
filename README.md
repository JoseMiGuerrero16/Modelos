# PROYECTO INF236 - GRUPO 10

## Integrantes

- José Guerrero C.
- Andrés Saldias S.
- Myckoll Winchester M.

## Instrucciones de uso

### Requerimientos

Este proyecto fue creado utilizando `Python 3.11`, por lo que se recomienda utilizar esta versión o una superior para su ejecución. También es necesario tener MongoDB.

### Instalación

Crear un entorno virtual para la ejecución del proyecto.

```bash
python -m venv .venv
```

Para activar el entorno virtual:

```bash
.venv\Scripts\activate
```

Instalar las dependencias del proyecto:

```bash
python -m pip install -r requirements.txt
```

### Tokens / Keys

Los tokens y las keys necesarias para la ejecución son dos (de momento), se pueden conseguir en los siguientes enlaces:

- [API de OpenAI](https://platform.openai.com/api-keys) (OPENAI_API_KEY)
- [API de Custom Search JSON](https://developers.google.com/custom-search/v1/overview?hl=es-419#api_key) (GOOGLE_API_KEY)
- [Crear un nuevo buscador](https://cse.google.com/cse/create/new) (CX)

Una vez obtenidos, se deben guardar en el archivo `.env` que debe ser añadido al directorio principal del proyecto, con el siguiente formato:

```env
OPENAI_API_KEY="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"
GOOGLE_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXX30hrwZnSe88"
CX="XXXXXXXXXXXX346eb"
```

### MongoDB

Se debe crear una base de datos llamada `Proyecto` (sensible a mayúsculas) y una colección llamada `Talleristas`.

### Ejecución

Ejecutamos la API con el siguiente comando:

```bash
uvicorn api:app --reload
```

y finalmente el proyecto con:

```bash
streamlit run Home.py
```
