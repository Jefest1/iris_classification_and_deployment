from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from flasgger import Swagger
import pandas as pd
import joblib
import numpy as np


# Loading the model
model = joblib.load('scripts/model.pkl')

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/predict', methods=['POST', 'GET'])
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
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')

    # convert collected data to an array
    data = np.array([[s_length, s_width, p_length, p_width]])

    # predicting the request
    pred = model.predict(data)
    return 'Prediction :{}'.format(pred)


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
    pred = model.predict(file)

    # return the result as a list
    return 'prediction : {}'.format(jsonify(pred.tolist()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
