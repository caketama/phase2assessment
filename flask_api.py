from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    return jsonify({"message": "hello"})


@app.route('/evens', methods=["POST"])
def evens():
    data = request.get_json()
    for data in data.values():
        for number in data:
            if number % 2 == 0:
                return jsonify({"evens": number})


@app.route('/odds', methods=["POST"])
def odds():
    data = request.get_json()
    for data in data.values():
        for number in data:
            if number % 3 == 0:
                return jsonify({"odds": number})


if __name__ == "__main__":
    app.run()
