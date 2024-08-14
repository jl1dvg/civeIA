from flask import Flask, request, jsonify

# Crear la aplicación Flask con el nombre personalizado 'civeIA'
app = Flask('civeIA')

@app.route('/trigger_click', methods=['POST'])
def trigger_click():
    # Recibir datos enviados desde la extensión o cualquier cliente
    data = request.json

    # Lógica que quieres implementar
    print(f"Received data: {data}")

    return jsonify({"status": "success", "message": "Click triggered in civeIA backend"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
