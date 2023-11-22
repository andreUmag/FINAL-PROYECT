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
    with open('backend/ply/entrada.txt', 'w') as file:
        file.write(texto)
    return jsonify({'mensaje': 'Texto guardado exitosamente'})

@app.route('/execute_code')
def execute_code():
    try:
        result = subprocess.check_output(['python', 'backend/ply/execute.py'], universal_newlines=True)
        return jsonify({'mensaje': result})
    except Exception as e:
        return jsonify({'mensaje': f'Error: {str(e)}'})
    
@app.route('/validate_code')
def validate_code():
        result = subprocess.check_output(['python', 'backend/ply/validate.py'], universal_newlines=True)
        return jsonify({'mensaje': result})

if __name__ == '__main__':
    app.run(debug=True)