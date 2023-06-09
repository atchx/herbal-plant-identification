from flask import Flask, render_template, jsonify, request
from markupsafe import Markup
from model import predict_image
import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")

@app.route('/pengembang')
def pengembang():
    return render_template('pengembang.html')

@app.route('/cara')
def cara():
    return render_template('cara.html')

if __name__ == "__main__":
    app.run(debug=True)
