from flask_restful import Resource, reqparse

class Pokedex(Resource):
    wikidex = [{'id':1, 'id_nacional': 257, 'pokemon': 'Blaziken', 'tipo': 'fuego', 'generación': 'Tercera'},
               {'id':2, 'id_nacional': 65, 'pokemon': 'Alakazam', 'tipo': 'psíquico', 'generación': 'Primera'},
               {'id':3, 'id_nacional': 376, 'pokemon': 'Metagross', 'tipo': 'Acero', 'generación': 'Tercera'},
              ]
    # {'id':5, 'id_nacional': 25, 'pokemon': 'Pikachu', 'tipo': 'eléctrico', 'generación': 'Tercera'},
    def get(self, id=1):
        id = int(id)
        if id == -1:
            return self.wikidex, 200
        elif id != -1 and id >= 1:
            for data in self.wikidex:
                if data['id'] == id:
                    return data, 200
            return {'mensaje': 'No se encontraron resultados'}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_nacional', type=int, required=True)
        parser.add_argument('pokemon', type=str, required=True)
        parser.add_argument('tipo', type=str, required=True)
        parser.add_argument('generación', type=str, required=True)
        args = parser.parse_args()
        identificador = len(self.wikidex)
        args['id'] = identificador + 1
        self.wikidex.append(args)
        return {'mensaje': 'ok'}, 200

    def put(self, id=-1):
        id = int(id)
        parser = reqparse.RequestParser()
        parser.add_argument('id_nacional', type=int, required=True)
        parser.add_argument('pokemon', type=str, required=True)
        parser.add_argument('tipo', type=str, required=True)
        parser.add_argument('generación', type=str, required=True)
        args = parser.parse_args()

        if id != -1 and id >= 1:
            for data in self.wikidex:
                if data['id'] == id:
                    data['id_nacional'] = args['id_nacional']
                    data['pokemon'] = args['pokemon']
                    data['tipo'] = args['tipo']
                    data['generación'] = args['generación']
                    return {'mensaje': 'Elemento editado'}, 200
            return {'mensaje': 'No se encontro el pokemon'}, 200
        return {'mensaje': 'Falta introducir una id correcta'}, 200

    def delete(self, id=-1):
        id = int(id)
        if id != -1 and id >= 1:
            indice = 0
            for data in self.wikidex:
                if data['id'] == id:
                    self.wikidex.pop(indice)
                    return {'mensaje': 'Elemento eliminado'}, 200
                indice = indice + 1
            return {'mensaje': 'No se encontro el pokemon'}, 200
        return {'mensaje': 'Falta introducir una id correcta'}, 200
