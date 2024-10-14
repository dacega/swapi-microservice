from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/people')
def get_people():
    """
    Obtiene datos de la API de Star Wars (con paginación), 
    los ordena por nombre y los devuelve en formato JSON.
    """
    try:
        people = []
        next_page = 'https://swapi.dev/api/people/'  # Empieza en la primera página

        while next_page:
            response = requests.get(next_page)
            response.raise_for_status()
            data = response.json()
            people.extend(data['results'])  # Agrega los personajes de la página actual
            next_page = data['next']  # Obtiene la URL de la siguiente página

        # Ordena la lista completa de personas por nombre
        people.sort(key=lambda person: person['name'])

        return jsonify(people)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error al obtener datos de la API: {e}")
        return jsonify({'error': 'No se pudieron obtener los datos'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
