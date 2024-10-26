from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Create a dictionary to map operation names to their corresponding functions
operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def do_math(operation):
    if operation in operations:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = operations[operation](a, b)
        return str(result)
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(debug=True)
