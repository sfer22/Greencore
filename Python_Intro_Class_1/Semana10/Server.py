import os
from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

persons = []


def id_exisits(id, persons):
    app.logger.debug("id_exists was called")
    app.logger.debug(id)
    app.logger.debug(persons)
    for person in persons:
        if person["id"] == id:
            return True

        return False


@app.route('/')
def get_root_resource():
    return 'This is a root resource'


@app.route('/api/v1/person', methods=["POST"])
def post_person():
    if not request.is_json:
        return jsonify({
            "msg": "only json is supported in this API"
        }), 400

    # Si llegamos aca es porque los datos si son JSON
    datos = request.get_json()

    # Para poder crear una persona (recurso) es mandadorio que tenga un id unico
    if "id" not in datos:
        return jsonify({
            "msg": "An id is required"
        }), 400

    if id_exisits(datos["id"], persons):
        return jsonify({
            "msg": "The provided id is already in use"
        }), 400

    persons.append(datos)

    return jsonify({
        "msg": "Person created"
    }), 201


@app.route('/api/v1/person', methods=["GET"])
def get_person():
    return jsonify(persons), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
