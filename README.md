# Proyecto INF236 Grupo 10

## Integrantes

- José Guerrero C.
- Andrés Saldias S.
- Myckoll Winchester M.

## Instrucciones de uso

### Requerimientos

Este proyecto fue creado utilizando Python 3.11, por lo que se recomienda utilizar esta versión o una superior para su ejecución.

Se recomienda (aunque no es necesario) utilizar un entorno virtual para la ejecución del proyecto.

```bash
python -m venv .venv
```

Para activar el entorno virtual:

- En Windows:

```bash
.venv\Scripts\activate
```

- En Linux:

```bash
source .venv/bin/activate
```

Finalmente, instalar las dependencias del proyecto:

```bash
python -m pip install -r requirements.txt
```

### Tokens / Keys

Los tokens y las keys necesarias para la ejecución son dos (de momento), se pueden conseguir en los siguientes enlaces:

- [API de Custom Search JSON](https://developers.google.com/custom-search/v1/overview?hl=es-419#api_key) (GOOGLE_API_KEY)
- [Crear un nuevo buscador](https://cse.google.com/cse/create/new) (CX)

Una vez obtenidos, se deben guardar en un archivo `.env` que debe ser añadido al directorio principal del proyecto, con el siguiente formato:

```env
GOOGLE_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXX30hrwZnSe88"
CX="XXXXXXXXXXXX346eb"
```
