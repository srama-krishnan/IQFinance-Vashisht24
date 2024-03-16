import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

def ValuePredictor(to_predict_list):
    to_predict = pd.DataFrame(to_predict_list)
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/', methods=['GET','POST'])
def predict():
    to_predict_list = request.form.to_dict(flat=False)  # Convert the form data into a dictionary, maintaining lists for multiple values
    to_predict_list = {k: v[0] if len(v) == 1 else v for k, v in to_predict_list.items()}  # Unpack lists if there's only one value per key
    to_predict_list = np.array(list(map(float, to_predict_list.values()))).reshape(1, -1)  # Convert all values to float and reshape to 2D
    result = ValuePredictor(to_predict_list)
    if int(result)==1:
        return 'The person is likely to experience financial distress'
    else:
        return 'The person is not likely to experience financial distress'

# @app.route('/predict', methods=['POST'])
# def predict():
#     to_predict_list = request.form.to_dict()
#     to_predict_list = list(to_predict_list.values())
#     to_predict_list = list(map(float, to_predict_list))
#     result = ValuePredictor(to_predict_list)
#     if int(result)==1:
#         prediction = 'The person is likely to experience financial distress'
#     else:
#         prediction = 'The person is not likely to experience financial distress'
#     return render_template('predict.html', prediction_text=prediction)


if __name__ == '__main__':
    app.run(debug=True)