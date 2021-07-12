from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        "Id": 1,
        "title": "study",
        'description': "I study a lot. I am in 10th. So i study.",
        'done': False
    },
    {
        "Id": 2,
        "title": "play",
        'description': "I play a lot. I have online school. So i play.",
        'done': True
    }
]

@app.route("/addData",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data",
        },400)
    task = {
        "Id": tasks[-1]['Id']+1,
        "title": request.json['title'],
        'description': request.json.get('description',''),
        'done': False,
    }
    tasks.append(task)
    return jsonify({"status":"success","message":"Task Added Successful"})

@app.route("/getData")
def get_data():
    return jsonify({"data":tasks})
app.run(debug=True)