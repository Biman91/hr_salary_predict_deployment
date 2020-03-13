# Import libraries
import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)                                   # create an app instance
model = pickle.load(open('model.pkl', 'rb'))            # load model

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():                                      # call method hellopickle.load(open('model.pkl', 'rb'))
    int_feat = [float(x) for x in request.form.values()]
    feat_sep = [np.array(int_feat)]
    prediction = model.predict(feat_sep)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f"Employee Salary should be {output} INR")


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app