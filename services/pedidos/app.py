from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/pedido")
def pedido():
    estoque = requests.get("http://estoque:5000/estoque").json()
    pagamento = requests.get("http://pagamentos:5000/pagamento").json()

    return jsonify({
        "pedido": "Pedido registrado",
        "estoque": estoque,
        "pagamento": pagamento
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)