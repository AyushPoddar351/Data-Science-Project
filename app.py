from flask import Flask , render_template , request , jsonify
import os, numpy as np, pandas as pd

from src.DataScienceProject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET'])

def home_page():
    return render_template('index.html')

@app.route('/train',methods=['GET'])

def train():
    os.system("python main.py")
    return "Training Successfull!"

@app.route('/predict',methods=['POST','GET'])

def predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed acidity'])
            volatile_acidity = float(request.form['volatile acidity'])
            citric_acid = float(request.form['citric acid'])
            residual_sugar = float(request.form['residual sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free sulfur dioxide'])
            total_sulfur_dioxide = float(request.form['total sulfur dioxide'])
            density = float(request.form['density'])
            ph = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol]
            data = np.array(data).reshape(1,-1)

            obj = PredictionPipeline()
            prediction = obj.predict(data)

            return render_template('results.html',prediction = str(prediction))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something went wrong'
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)