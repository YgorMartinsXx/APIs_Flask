from flask import Flask, jsonify, request
import modelTinder as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def ola():
    return "servidor do tinder"

@app.route("/pessoas", methods = ['GET'])
def todas_pessoas():
    return i.todas_as_pessoas()

@app.route("/pessoas/<int:id>", methods = ['GET'])
def pessoas_por_id(id):
    try:
        return i.localiza_pessoa(id)
    except i.NotFoundError:
        return {"erro:" "id invalida" },404

@app.route("/pessoas", methods = ["POST"])
def adiciona_pessoa():
    try:
        dicionario_enviado = request.json
        return i.adiciona_pessoa(dicionario_enviado)
    except i.NotFoundError:
        return {"erro:" "id invalida" },404
    
    
@app.route("/pessoas/reseta", methods = ['POST'])
def reseta():
    i.reseta()
    return i.todas_as_pessoas()

@app.route("/sinalizar_interesse/<int:p1>/<int:p2>", methods = ['PUT'])
def add_like(p1,p2):
    i.adiciona_interesse(p1,p2)
    d = {f"interesses {p1}": i.consulta_interesses(p1)}
    return d

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)