from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/guardar_texto', methods=['POST'])
def guardar_texto():
    data = request.get_json()
    texto = data.get('texto', '')

    # Guardar el texto en el archivo
    with open('backend/ply/entrada.txt', 'w') as file:
        file.write(texto)

    return jsonify({'mensaje': 'Texto guardado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)