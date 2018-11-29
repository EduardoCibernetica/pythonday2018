from flask_restful import Resource, reqparse

class Pokedex(Resource):
    wikidex = [{'id':1, 'id_nacional': 257, 'pokemon': 'Blaziken', 'tipo': 'fuego', 'generación': 'Tercera'},
               {'id':2, 'id_nacional': 65, 'pokemon': 'Alakazam', 'tipo': 'psíquico', 'generación': 'Primera'},
               {'id':3, 'id_nacional': 376, 'pokemon': 'Metagross', 'tipo': 'Acero', 'generación': 'Tercera'},
              ]
    def get(self, id_nacional=None):
        if id_nacional == None:
            return self.wikidex, 200
        elif id_nacional != None and id_nacional >= 1:
            for data in self.wikidex:
                if data['id_nacional'] == id_nacional:
                    return data, 200
            return {'mensaje':
                    'No tenemos información del pokemon {} en nuestra wikidex'.format(id_nacional)}, 200

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
        return {'mensaje': 'El pokemon {} fue añadido a la wikidex'.format(args['pokemon'])}, 200

    def put(self, id_nacional=None):
        parser = reqparse.RequestParser()
        parser.add_argument('id_nacional', type=int, required=True)
        parser.add_argument('pokemon', type=str, required=True)
        parser.add_argument('tipo', type=str, required=True)
        parser.add_argument('generación', type=str, required=True)
        args = parser.parse_args()

        if id_nacional != None and id_nacional >= 1:
            for data in self.wikidex:
                if data['id_nacional'] == id_nacional:
                   data['pokemon'] = args['pokemon']
                   data['tipo'] = args['tipo']
                   data['generación'] = args['generación']
                   return {'mensaje': 'El pokemon {} fue editado'.format(data['pokemon'])}, 200
            return {'mensaje': 'No se encontro el pokemon'}, 200
        return {'mensaje': 'Falta introducir una id_nacional correcta'}, 200

    def delete(self, id_nacional=None):
        if id_nacional != None and id_nacional >= 1:
            indice = 0
            for data in self.wikidex:
                if data['id_nacional'] == id_nacional:
                    self.wikidex.pop(indice)
                    return {'mensaje': 'El pokemon {} fue eliminado'.format(data['pokemon'])}, 200
                indice = indice + 1
            return {'mensaje': 'No tenemos informaión en nuestra Wikidex'}, 200
        return {'mensaje': 'Falta introducir una id_nacional valido'}, 200
