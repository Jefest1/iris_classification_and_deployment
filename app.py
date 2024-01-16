from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib
import numpy as np


app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
#  Creating a predict fucntion
def predict():
    # Getting the data
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_lenght = request.args.get('p_length')
    p_width = request.args.get('p_width')

    # Scaler the data
    scaler = StandardScaler()
    data = np.array([[s_length, s_width, p_lenght, p_width]])

    # Loading the model
    model = joblib.load('model.pkl')

    # predicting the request
    pred = model.predict(data)
    return str(pred)


@app.route('/predict_file', methods=['POST', 'GET'])
def predict_file():
    # Get the file
    file = pd.read_csv(request.files.get('test.csv'), header=None)

    # scale the data
    scaler = StandardScaler()
    file = scaler.fit_transform(file)

    # predict the types of flowers
    model = joblib.load('model.pkl')
    pred = model.predict(file)

    # return the result
    return jsonify({'prediction': pred.tolist()})


if __name__ == '__main__':
    app.run()
