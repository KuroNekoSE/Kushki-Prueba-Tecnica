import json
import logging
import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()

PUBLIC_KEY = os.getenv("KUSHKI_PUBLIC_KEY")
PRIVATE_KEY = os.getenv("KUSHKI_PRIVATE_KEY")
BASE_URL = os.getenv("KUSHKI_BASE_URL", "https://api-uat.kushkipagos.com")

# El monto lo fija el servidor, no el navegador.
AMOUNT = 1000
CURRENCY = "MXN"

app = Flask(__name__, static_folder="static", static_url_path="")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[logging.FileHandler("kushki.log"), logging.StreamHandler()],

)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/config")
def config():
    return jsonify({"publicKey": PUBLIC_KEY, "amount": AMOUNT, "currency": CURRENCY})


@app.route("/api/charge", methods=["POST"])
def charge():
    data = request.get_json(silent=True) or {}
    token = data.get("token")
    if not token:
        return jsonify({"status": "error", "message": "Falta el token."}), 400

    payload = {
        "token": token,
        "amount": {
            "subtotalIva": 0,
            "subtotalIva0": AMOUNT,
            "ice": 0,
            "iva": 0,
            "currency": CURRENCY,
        },
        "fullResponse": True,
    }
    headers = {
        "Content-Type": "application/json",
        "Private-Merchant-Id": PRIVATE_KEY,
    }

    try:
        resp = requests.post(
            f"{BASE_URL}/card/v1/charges", json=payload, headers=headers, timeout=30
        )
    except requests.Timeout:
        logging.error("Timeout al cobrar con Kushki")
        return jsonify({
            "status": "uncertain",
            "message": "Kushki no respondió a tiempo. Verifica la transacción antes de reintentar.",
        }), 504
    except requests.RequestException as error:
        logging.error("Error de conexión con Kushki: %s", error)
        return jsonify({"status": "error", "message": "No se pudo contactar a Kushki."}), 502

    try:
        body = resp.json()
    except ValueError:
        body = {}

    logging.info("charge HTTP %s %s", resp.status_code, json.dumps(body))

    if resp.status_code == 200 and body.get("ticketNumber"):
        return jsonify({"status": "approved", "ticketNumber": body["ticketNumber"]})

    return jsonify({
        "status": "declined",
        "code": body.get("code"),
        "message": body.get("message", "Transacción rechazada."),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)