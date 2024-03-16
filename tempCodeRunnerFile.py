import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta
# Load the dataset
data_path = 'HDFC.csv'  # Replace with the path to your dataset
data = pd.read_csv(data_path)

# Prepare the data
data['Date'] = pd.to_datetime(data['Date']).dt.date
data.set_index('Date', inplace=True)
close_series = data['Close']

# Define the ARIMA model with a higher order and fit it
model = ARIMA(close_series, order=(30,1,0))  # Increased order
model_fit = model.fit()

# Forecast the next 100 days
forecast = model_fit.forecast(steps=30)

# Prepare the new index (dates) for the forecasted values
last_date = close_series.index[-1]
forecast_dates = [last_date + timedelta(days=i) for i in range(1, 31)]

# Creating a DataFrame for the forecasted values
forecast_df = pd.DataFrame({
    'Date': forecast_dates,
    'Close': forecast
})
forecast_df.set_index('Date', inplace=True)

# Save the forecast to a new CSV file
forecast_df.to_csv('Book1.csv')
book1_data = pd.read_csv('Book1.csv')
book1_data['Date'] = pd.to_datetime(book1_data['Date'])
book1_data.set_index('Date', inplace=True)
hdfc_data = pd.read_csv('HDFC.csv')
# Merge the original dataset with the forecasted data
merged_data = pd.concat([hdfc_data, book1_data], axis=0).drop_duplicates()

# You can save the merged dataset to a new file or overwrite the HDFC.csv if needed
merged_data_path = 'HDFC.csv'
merged_data.to_csv(merged_data_path)