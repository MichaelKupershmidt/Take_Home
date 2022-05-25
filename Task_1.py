import flask
from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/healthz')
def healthz():
    return ''


@app.route("/accounts")
def accounts():
    d = {
  "accounts": [
    { "id": "0", "firstname": "Pooh", "lastname": "Shiesty" },
    { "id": "1", "firstname": "Albert", "lastname": "Einstein" },
    { "id": "2", "firstname": "Vitalik", "lastname": "Buterin" }
  ]
}
    return jsonify(d)
if __name__ == '__main__':
    app.run(port=8080)