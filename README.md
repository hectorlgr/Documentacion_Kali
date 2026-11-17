
# Proyecto Flask - Documentacion

## Descripcion

Proyecto de ejemplo desarrollado en Python utilizando
Flask para demostrar buenas practicas de documentacion
y trazabilidad en el desarrollo de software.

## Objetivos

- Documentar el codigo fuente.
- Generar documentacion HTML mediante Doxygen.
- Gestionar los cambios utilizando Git.
- Automatizar la documentacion utilizando Jenkins.
- Desplegar la aplicacion en un entorno de prueba.

## Tecnologias utilizadas

- Kali Linux
- Python
- Flask
- Git
- Docker
- Jenkins
- Doxygen
- Graphviz

## Rutas disponibles

### Ruta principal

GET /

Devuelve un mensaje de bienvenida.

### Ruta de saludo

GET /hello?name=Kali

Devuelve un saludo personalizado en formato JSON.

## Generacion de documentacion

La documentacion tecnica se genera ejecutando:

    doxygen Doxyfile

El resultado se almacena en:

    docs/html/

## Trazabilidad

Los cambios del codigo y de la documentacion
se gestionan mediante Git y GitHub.
