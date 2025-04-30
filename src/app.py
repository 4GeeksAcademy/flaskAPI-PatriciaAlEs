from flask import Flask, jsonify
app = Flask(__name__)
from flask import request


todos = [
    { "label": "Mi primera tarea", "done": False },
    { "label": "Mi segunda tarea", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # Puedes convertir esa variable en una cadena json de la siguiente manera
    json_text = jsonify(todos)

    # Y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  
    return jsonify(todos)       



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Esta es la posición a eliminar:", position)
    todos.pop(position)   
    return jsonify(todos) # <-- Devuelve la lista actualizada


# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)