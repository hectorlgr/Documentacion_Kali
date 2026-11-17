
"""
@file app.py
@brief Aplicacion Flask para la guia 3.4.2.

@details
Aplicacion utilizada para demostrar la generacion
automatica de documentacion y su integracion con
Git, Doxygen y Jenkins.
"""

from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def index():
    """
    @brief Muestra la pagina principal de la aplicacion.

    @details
    Devuelve un mensaje que identifica el proyecto
    de gestion de dependencias.

    @return Mensaje de texto de bienvenida.
    """
    return "Aplicación de ejemplo para gestión de dependencias"


@app.get("/hello")
def hello():
    """
    @brief Genera un saludo personalizado.

    @details
    Obtiene el nombre desde el parametro de consulta
    HTTP llamado 'name'. Si no se proporciona,
    utiliza el valor predeterminado 'mundo'.

    Ejemplo:
    /hello?name=Kali

    @return Respuesta JSON con el mensaje de saludo.
    """
    nombre = request.args.get("name", "mundo")
    return {"mensaje": f"Hola, {nombre}!"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
