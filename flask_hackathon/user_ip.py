import pandas as pd
import joblib

# Function to take user inputs
def take_user_inputs(df):
    inputs = {}
    for column in df.columns:
        if column != 'SeriousDlqin2yrs':  # Exclude the target column
            inputs[column] = input(f"Enter value for {column}: ")
    return inputs

# Function to preprocess user inputs
def preprocess_inputs(inputs, df):
    # Convert inputs to DataFrame
    inputs_df = pd.DataFrame([inputs])

    # Reorder columns to match the training data
    inputs_df = inputs_df[df.columns[:-1]]

    # Add missing columns, if any
    missing_columns = set(df.columns) - set(inputs_df.columns)
    for col in missing_columns:
        inputs_df[col] = 0  # You can set any default value here, like 0 or mean value

    return inputs_df

# Function to make predictions
def predict(model_path, inputs_df):
    # Load the trained model
    model = joblib.load(model_path)

    # Make predictions
    predictions = model.predict(inputs_df)

    return predictions

df_test = pd.read_csv("GMSC-testing.csv")
df_test = df_test.drop(df_test.columns[0], axis=1)
df_test = df_test.drop(df_test.columns[0], axis=1)
df_test = df_test.fillna(df_test.mean())
df_test = df_test.drop(["age"], axis=1)

# Load the trained model
model = joblib.load('trained_model.pkl')

# Take user inputs
user_inputs = take_user_inputs(df_test)

# Preprocess inputs
processed_inputs = preprocess_inputs(user_inputs, df_test)

# Make predictions
predictions = predict("trained_model.pkl", processed_inputs)

# Output the predictions
print("Prediction:", predictions)