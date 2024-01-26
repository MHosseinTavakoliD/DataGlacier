from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, static_url_path='/static')

def Prediction_function(features):
    # Assuming features is a list of [x, y, z]
    return sum(features)

@app.route('/')  # Home route
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting values and converting them to integers
        x_value = int(request.form['x-value'])
        y_value = int(request.form['y-value'])
        z_value = int(request.form['z-value'])
    except ValueError:
        # Handle the case where conversion fails
        return render_template('index.html', prediction_text='Please enter valid integers for X, Y, and Z.')

    int_features = [x_value, y_value, z_value]
    prediction = Prediction_function(int_features)
    output = round(prediction, 2)

    # Include the input values in the render_template call
    return render_template('index.html', prediction_text='The summation is {}'.format(output),
                           x_value=x_value, y_value=y_value, z_value=z_value)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
