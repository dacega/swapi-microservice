from flask import Flask
from flask_restx import Api, Resource, fields
import requests

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Star Wars',
          description='Microservicio que consume la API de Star Wars y ordena los datos por nombre')

ns = api.namespace('people', description='Operaciones relacionadas con los personajes')

@ns.route('')
class PeopleList(Resource):
    @ns.doc('Obtener lista de personajes')
    def get(self):
        """
        Obtiene datos de la API de Star Wars (con paginación), 
        los ordena por nombre y los devuelve en formato JSON.
        """
        try:
            people = []
            next_page = 'https://swapi.dev/api/people/'

            while next_page:
                response = requests.get(next_page)
                response.raise_for_status()
                data = response.json()
                people.extend(data['results'])
                next_page = data['next']

            people.sort(key=lambda person: person['name'])

            return people
        except requests.exceptions.RequestException as e:
            app.logger.error(f"Error al obtener datos de la API: {e}")
            return {'error': 'No se pudieron obtener los datos'}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
