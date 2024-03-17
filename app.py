import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
loaded_model = joblib.load('trained_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data and convert to numeric values
        to_predict_list = [
            float(request.form['RevolvingUtilizationOfUnsecuredLines']),
            int(request.form['NumberOfTime3059DaysPastDueNotWorse']),
            float(request.form['DebtRatio']),
            int(request.form['MonthlyIncome']),
            int(request.form['NumberOfOpenCreditLinesAndLoans']),
            int(request.form['NumberOfTimes90DaysLate']),
            int(request.form['NumberRealEstateLoansOrLines']),
            int(request.form['NumberOfTime6089DaysPastDueNotWorse']),
            int(request.form['NumberOfDependents'])
        ]
        # Convert the list to numpy array and reshape it
        to_predict = np.array(to_predict_list).reshape(1, -1)
        # Make prediction
        result = ValuePredictor(to_predict)
        # Pass the prediction result to the template
        return render_template('templates\index.html', prediction=result)
    return render_template('templates\index.html')

def ValuePredictor(to_predict):
    result = loaded_model.predict(to_predict)
    return result[0]

if __name__ == '__main__':
    app.run(debug=True)