from flask import Flask, request
from sklearn.preprocessing import StandardScaler
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


if __name__ == '__main__':
    app.run()
