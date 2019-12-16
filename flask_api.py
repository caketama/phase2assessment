from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    return jsonify({"message": "hello"})


@app.route('/evens', methods=["GET"])
def evens():
    data = request.get_json()
    return data


if __name__ == "__main__":
    app.run()
