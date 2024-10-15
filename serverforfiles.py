# Dependencias necesarias
# pip install flask

from flask import Flask, request, redirect, send_from_directory, render_template_string
import os

app = Flask(__name__)
CARPETA_DESCARGAS = r'C:\EXAMPLE'  # Usa la ruta que has creado

if not os.path.exists(CARPETA_DESCARGAS):
    os.makedirs(CARPETA_DESCARGAS)

# Ruta principal para subir y listar archivos
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        archivo = request.files['file']
        if archivo:
            ruta_archivo = os.path.join(CARPETA_DESCARGAS, archivo.filename)
            archivo.save(ruta_archivo)
            return redirect('/')
    return '''
    <!doctype html>
    <title>Subir y Descargar Archivos</title>
    <h1>Subir un archivo</h1>
    <form action="/" method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value="Subir">
    </form>
    <h2>Archivos disponibles:</h2>
    <ul>
      ''' + ''.join([f'<li><a href="/{f}">{f}</a></li>' for f in os.listdir(CARPETA_DESCARGAS)]) + '''
    </ul>
    '''

# Ruta para descargar archivos directamente desde la raíz
@app.route('/<filename>')
def archivo_subido(filename):
    return send_from_directory(CARPETA_DESCARGAS, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
