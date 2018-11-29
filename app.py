from flask import Flask
from flask_restful import Resource, Api
from recursos.pokedex import Pokedex

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokedex, '/pokemon',
                          '/pokemon/<string:id>')

if __name__ == '__main__':
    app.run(debug=True, port=6000)
