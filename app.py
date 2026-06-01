from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensaje": "¡API funcionando!", "status": "ok"})

@app.route('/usuarios')
def usuarios():
    return jsonify([
        {"id": 1, "nombre": "Cristian"},
        {"id": 2, "nombre": "Pablo"}
    ])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)