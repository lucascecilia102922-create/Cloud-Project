from flask import Flask
import requests

app = Flask(__name__)

@app.route("/pedido")
def gateway():
    resposta = requests.get("http://pedidos:5000/pedido")
    return resposta.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)