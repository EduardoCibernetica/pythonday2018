from flask import Flask
from flask_restful import Api

from recursos.pokedex import Pokedex

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokedex, '/pokemon',
                          '/pokemon/<int:id_nacional>')

if __name__ == '__main__':
    app.run()
