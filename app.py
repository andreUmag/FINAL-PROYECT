from flask import Flask, render_template, request, jsonify
import subprocess


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

@app.route('/execute_code')
def execute_code():
    try:
        # Ejecutar el código desde el archivo principal.py y capturar la salida
        result = subprocess.check_output(['python', 'backend/ply/principal.py'], universal_newlines=True)

        # Devolver la salida como JSON
        return jsonify({'mensaje': result})
    except Exception as e:
        return jsonify({'mensaje': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)