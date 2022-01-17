from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "Contact": "99876444560",
        "Name": "Raju Rastogi",
        "done": False
    },
    {
        "id": 2,
        "Contact": "9876543222",
        "Name": "Farhan Qureshi",
        "done": False
    },
]


@app.route("/add-data", methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            "Status": "Error 400",
            "Message": "Data not Provided"
        }, 400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "Status": "Sucess",
        "Message": "Task Added Sucessfully"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data":contacts
    })

if __name__=="__main__":
    app.run(debug=True)
