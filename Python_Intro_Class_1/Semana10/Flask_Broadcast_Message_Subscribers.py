import os
from flask import Flask, jsonify, request

app = Flask("EvilApi")
app.debug = True

subscribers = []


def ip_exists(ip, subscribers):
    app.logger.debug("ip_exists was called")
    app.logger.debug(ip)
    app.logger.debug(subscribers)
    if ip in subscribers:
            return True
    return False


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

    if ip_exists(datos["ip"], subscribers):
        return jsonify({
            "msg": "The provided IP address is already subscribed"
        }), 400

    subscribers.append(datos["ip"])

    return jsonify({
        "msg": "Your IP address is now subscribed"
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
