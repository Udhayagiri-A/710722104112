from flask import Flask, jsonify
import random
app = Flask(__name__)
@app.route('/numbers/<number_id>', methods=['GET'])
def numbers(number_id):
    map = {
        "p": [2, 3, 5, 7, 11, 13, 17,19,23],
        "f": [0, 1, 1, 2, 3, 5, 8, 13,21],
        "e": [2, 4, 6, 8, 10, 12, 14,16,18,20],
        "o": [1, 3, 5, 7, 9, 11, 13,15,17,19]
    }
    num = map.get(number_id, [])
    if not num:
        return jsonify({"error": "Invalid ID"}), 400
    response = {
        "numbers": random.sample(num, min(4, len(num)))
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True, port=9876)