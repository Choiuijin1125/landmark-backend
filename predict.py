from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
import os
import model


app = Flask(__name__, template_folder='Template')
cors = CORS(app)
Bootstrap(app)

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return result


if __name__ == '__main__':
    app.run(debug = True)        