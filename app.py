from flask import Flask, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0,'nome':'Helson','habilidades':['Python','Flask']},
    {'id':1,'nome':'Kattiele','habilidades':['JavaScript','UX/UI']}
]
#devolve um desenvolvedor pelo id, altera e deleta
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE']) #o rota após o fim da url ex : pichau.com/dev
def desenvolvedor(id):
    if request.method =='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'erro','mensagem':mensagem}
        except  Exception:
            mensagem = 'Erro Desconhecido. Procure o Administrador da API '
            response = {'status':'erro','mensagem':mensagem}
        return (response)
    elif request.method =='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem':'Registro Excluído'}
#lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method =='POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    elif request.method =='GET':
        return desenvolvedores


if __name__== '__main__':
    app.run(debug=True)

