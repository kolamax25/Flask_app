from flask import Flask, jsonify, request

app = Flask(__name__)

datas = [
    {
        'contact': '9987644456',
        'Name' : u'Buy groceries',
        'id': 1,
        'done'  :False

    },
    {

        'contact': 2,
        'Name': u'Learn Python',
        'id': 2, 
        'done': False        

    }
]

@app.route("/")
def hello_world():
    return "Hello Friend!"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data!"
        },400)

    data = {
        'contact': request.json['contact'],
        'Name': request.json.get('Name', ""),
        'id': datas[-1]['id'] + 1,
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })


@app.route("/get-data")
def getTask():
    return jsonify({
        "data" : datas
    })

if (__name__ == "__main__"):
    app.run(debug=True)
