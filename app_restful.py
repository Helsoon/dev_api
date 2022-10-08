import json

from flask import Flask , request
from flask_restful import Resource, Api
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0, 'nome': 'Helson', 'habilidades': ['Python', 'Flask']},
    {'id': 1, 'nome': 'Kattiele', 'habilidades': ['JavaScript', 'UX/UI']}
]


class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except  Exception:
            mensagem = 'Erro Desconhecido. Procure o Administrador da API '
            response = {'status': 'erro', 'mensagem': mensagem}
        return (response)

    def put(self,id):
       dados = json.loads(request.data)
       desenvolvedores[id] = dados
       return dados


    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro Excluído'}


#lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedore(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/de/<int:id>/')
api.add_resource(ListaDesenvolvedore, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
