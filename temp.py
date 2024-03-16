import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta

# Load the dataset
data_path = 'HDFC.csv'  # Replace with the path to your dataset
data = pd.read_csv(data_path)
data = data[['Date', 'Close']]  # Keep only Date and Close

# Prepare the data
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
close_series = data['Close']

# Define the ARIMA model with a higher order and fit it
model = ARIMA(close_series, order=(60,1,0))  # Increased order
model_fit = model.fit()

# Forecast the next 30 days
forecast = model_fit.forecast(steps=30)

# Prepare the new index (dates) for the forecasted values
last_date = data.index[-1]  # Using data.index since it's already the Date column
forecast_dates = [last_date + timedelta(days=i) for i in range(1, 31)]

# Creating a DataFrame for the forecasted values
forecast_df = pd.DataFrame({
    'Date': forecast_dates,
    'Close': forecast
})

# Formatting Date in forecast_df to ensure it's just the date (no time)
forecast_df['Date'] = pd.to_datetime(forecast_df['Date']).dt.date
forecast_df.set_index('Date', inplace=True)

# Save the forecast to a new CSV file
forecast_df.to_csv('Book1.csv', index=True)

# Now merge the forecast back to the original dataset
# Reload the original data to ensure it's in the correct format
data = pd.read_csv(data_path, usecols=['Date', 'Close'])
data['Date'] = pd.to_datetime(data['Date']).dt.date  # Ensuring the Date is in the correct format

# Concatenate the original data with the forecasted data
merged_data = pd.concat([data, forecast_df.reset_index()])
merged_data.drop_duplicates(subset='Date', keep='last', inplace=True)  # Removing duplicate dates if any

# Save the merged data back to HDFC.csv or another file as needed
merged_data.to_csv('HDFC.csv', index=False)
