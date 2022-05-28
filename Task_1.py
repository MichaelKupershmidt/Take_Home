import flask
from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/healthz')
def healthz():
    return ''


@app.route("/accounts/<id>")
def accounts(id):
    ih = int(id)
    d = {
  "accounts": [
    { "id": "0", "firstname": "Pooh", "lastname": "Shiesty" },
    { "id": "1", "firstname": "Albert", "lastname": "Einstein" },
    { "id": "2", "firstname": "Vitalik", "lastname": "Buterin" }
  ]
}
    if not ih>-1:
        return jsonify(d)
    elif not ih in d['accounts']:
        return "",404
    else: 
        j = d['accounts'][ih]
        return jsonify(j)

app.run(port=8080)



#not sure if this is also potential answer for level 2
    # try:
    #     ih = int(id)
        
    #     if not ih>-1:
    #         return jsonify(d)
    #     else: 
    #         j = d['accounts'][ih]
    #         return jsonify(j)
    # except Exception:
    #     raise abort(404)