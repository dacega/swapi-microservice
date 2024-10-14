from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/swapi/<resource>/<int:id>')
def get_swapi_resource(resource, id):
    """
    Obtiene datos de la API de Star Wars para un recurso e ID especifos.
    """
    try:
        response = requests.get(f'https://swapi.dev/api/{resource}/{id}')
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error al obtener datos de la API: {e}")
        return jsonify({'error': 'No se pudieron obtener los datos'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Especificar host='0.0.0.0' para que sea accesible desde fuera del contenedor
