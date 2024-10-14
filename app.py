from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/people')
def get_people():
    """
    Obtiene datos de la API de Star Wars, los ordena por nombre 
    y los devuelve en formato JSON.
    """
    try:
        response = requests.get('https://swapi.dev/api/people/')
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        data = response.json()
        people = data['results']

        # Ordena la lista de personas por nombre en orden ascendente
        people.sort(key=lambda person: person['name'])  

        return jsonify(people)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error al obtener datos de la API: {e}")
        return jsonify({'error': 'No se pudieron obtener los datos'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
