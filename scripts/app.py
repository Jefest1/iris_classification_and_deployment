from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from flasgger import Swagger
import pandas as pd
import joblib
import numpy as np


app = Flask(__name__)
swagger = Swagger(app)


@app.route('/predict', methods=['POST'])
#  Creating a predict fucntion
def predict():
    """This is an example endpoint for predicting Iris species
    ---
    parameters:
        - name: s_length
          in: query
          type: number
          required: true

        - name: s_width
          in: query
          type: number
          required: true

        - name: p_length
          in: query
          type: number
          required: true

        - name: p_width
          in: query
          type: number
          required: true
    """
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_lenght = request.args.get('p_length')
    p_width = request.args.get('p_width')

    # Scaler the data
    scaler = StandardScaler()
    data = np.array([[s_length, s_width, p_lenght, p_width]])

    # Loading the model
    model = joblib.load('scripts/model.pkl')

    # predicting the request
    pred = model.predict(data)
    return 'pred :', pred


@app.route('/predict_file', methods=['POST'])
def predict_file():
    """This is an example endpoint that accepts a file as input and returns a list of predictions
    ---
    parameters:
        - name: test.csv
          in: formData
          type: file
          required: true
    """
    # Get the file
    file = pd.read_csv(request.files.get('test.csv'), header=None)

    # scale the data
    scaler = StandardScaler()
    file = scaler.fit_transform(file)

    # predict the types of flowers
    model = joblib.load('scripts/model.pkl')
    pred = model.predict(file)

    # return the result
    return 'prediction :', pred.tolist()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
