import os
from flask import Flask, jsonify, request

app = Flask("EvilApi")

subscribers = []

@app.route('/')
def get_root_resource():
    return 'This is a root resource'

@app.route('/api/v1/subscriber', methods=["POST"])
def post_subscriber():
    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400

    datos = request.get_json()

    if "ip" not in datos:
        return jsonify({
            "msg": "An IP is required"
        }), 400

    if id_exists(datos["id"], persons):
        return jsonify({
            "msg": "The provided id is already in use"
        }), 400

    subscribers.append(datos["ip"])

    return jsonify({
        "msg": "su direccion IP ha sido suscrita"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)