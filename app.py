from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuración de Swagger UI
SWAGGER_URL = '/docs'  # URL donde estará disponible la documentación
API_URL = '/swagger.yaml'  # Archivo de especificación de Swagger
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Endpoint del Webhook
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Obtener los datos de la solicitud
    data = request.get_json()

    # Procesar los datos recibidos
    name = data.get('name', 'World')

    # Responder con un mensaje
    response = {
        'message': f'Hola, {name}!'
    }
    return jsonify(response), 200


# Endpoint para servir el archivo Swagger
@app.route('/swagger.yaml', methods=['GET'])
def serve_swagger():
    with open('swagger.yaml', 'r') as file:
        return file.read(), 200, {'Content-Type': 'application/x-yaml'}


if __name__ == '__main__':
    app.run(debug=True)
