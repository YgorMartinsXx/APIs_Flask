#essa parte é sempre igual, nao encana
from flask import Flask, request
app = Flask(__name__)
#fim da burocracia


#tudo que voce precisa de flask
@app.route("/proximo/<int:n>", methods=['GET'])
def proximo(n):
    if n < 10:
        return ({"erro":"numero muito pequeno"}),400
    return {"proximo numero":n+1}


@app.route("/receba", methods=['PUT',"POST"])
def receberei():
    print(request.json)
    return 'veja no cmd'


# essa parte é sempre igual, nao encana    
if __name__ == "__main__":
    app.run(debug=True, port = 5000)
#fim da burocracia
