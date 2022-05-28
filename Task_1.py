import flask
from flask import jsonify, abort, request, make_response
import json
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
app = flask.Flask(__name__)
app.config["DEBUG"] = True
d = {
  "accounts": [
    { "id": "0", "firstname": "Pooh", "lastname": "Shiesty" },
    { "id": "1", "firstname": "Albert", "lastname": "Einstein" },
    { "id": "2", "firstname": "Vitalik", "lastname": "Buterin" }
  ]
    }

@app.route('/healthz')
def healthz():
    return ''

@app.route("/accounts")
def accounts_no_id():
    return jsonify(d)

@app.route("/accounts/<id>")
def accounts(id):
    try:
        ih = int(id)
        j = d['accounts'][ih]
        return jsonify(j)
    except Exception:
        raise abort(404)
@app.route("/accounts/<id>/update", methods=['POST'])
def accounts_update(id):
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            data = Convert(data)
            ih = int(id)
            j = d['accounts'][ih]
        except Exception:
            raise abort(404)
        try:
            for key in j.keys():
                j[key] = data[key]
            d['accounts'][ih] = j
            return make_response(jsonify(d), 200)

        except Exception:
            raise abort(400)

@app.route('/post', methods=['POST'])
def post_route():
    if request.method == 'POST':

        data = dict(request.get_json(force=True))
        #data.json()
        data = Convert(data)
        #print('Data Received: "{data}"'.format(data=data))
        return "Request Processed.\n"

app.run(port=8080)


# curl localhost:8080/accounts/0 

# curl -v -X POST localhost:8080/accounts/0/update -d '{ "abc": "xyz" } 

# curl -v -X POST localhost:8080/accounts/0/update -d "{ \"firstname\": \"John\", \"lastname\": \"Smith\" }" 

# curl localhost:8080/accounts/0 

# curl -v -X POST localhost:8080/accounts/0/update -d '{ "firstname": "Jane" } 

# curl localhost:8080/accounts/0 
# curl -v -X POST localhost:8080/accounts/0/update -d '{ "lastname": "Doe" }

# curl localhost:8080/accounts/0 
