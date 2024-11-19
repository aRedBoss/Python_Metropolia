from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    result = is_prime(number)
    response = {
        "Number": number,
        "isPrime": result
    }
    return jsonify(response), 200

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
