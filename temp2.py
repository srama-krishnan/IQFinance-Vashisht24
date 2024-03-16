from sklearn.linear_model import LinearRegression
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta
import numpy as np

# Load the dataset
data_path = 'HDFC.csv'  # Replace with the path to your dataset
data = pd.read_csv(data_path)
data = data[['Date', 'Close']]  # Keep only Date and Close

# Parameters
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Load your data
# data = pd.read_csv('HDFC.csv')
# data = data['Close'].values
data = pd.read_csv('HDFC.csv')['Close'].values

# Use the last 5300 data points
data_recent = data[-5300:]

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data_recent.reshape(-1, 1))

# Data preparation
def create_dataset(dataset, look_back=1):
    X, y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(y)

look_back = 60
X, y = create_dataset(scaled_data, look_back)
X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

# Split the data into train and test sets
train_size = int(len(X) * 0.67)
test_size = len(X) - train_size
trainX, trainY = X[0:train_size,:,:], y[0:train_size]
testX, testY = X[train_size:len(X),:,:], y[train_size:len(y)]

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(1, look_back)))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(trainX, trainY, epochs=5, batch_size=1, verbose=1)

# Making predictions
last_window = testX[-1].reshape(1, 1, look_back)
future_predictions_scaled = []

for _ in range(500):  # predict the next 500
    next_val_scaled = model.predict(last_window)
    future_predictions_scaled.append(next_val_scaled[0][0])
    new_window = np.append(last_window[0][0][1:], next_val_scaled[0][0]).reshape(1, 1, look_back)
    last_window = new_window

future_predictions = scaler.inverse_transform(np.array(future_predictions_scaled).reshape(-1, 1))

# Print the first 10 predictions
print(future_predictions[:500])
