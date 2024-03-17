import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__, template_folder='templates', static_folder='templates/static')

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
            int(request.form['NumberOfDependents']),
        ]
        # Convert the list to numpy array and reshape it
        to_predict = np.array(to_predict_list).reshape(1, -1)
        # Make prediction
        result = ValuePredictor(to_predict)
        # Pass the prediction result to the template
        return render_template('predict.html', prediction=result)
    return render_template('index.html',prediction='')

def ValuePredictor(to_predict):
    result = loaded_model.predict(to_predict)
    if int(result[0]) == 1:
        return """Our analysis indicates that you may be at risk of experiencing financial distress in the near future. This could be due to a variety of factors, such as high debt levels, late payments, or a lack of financial resources. It's important to take proactive steps to address these issues and avoid potential financial pitfalls."""
    else:
        return """Our analysis indicates that you are not at risk of experiencing financial distress in the near future. However, it's important to continue managing your finances responsibly and to be aware of potential risks that could impact your financial stability."""

if __name__ == '__main__':
    app.run(debug=True)