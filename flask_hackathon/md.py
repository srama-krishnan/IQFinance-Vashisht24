import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load training data
df_train = pd.read_csv("GMSC-training.csv")
df_test = pd.read_csv("GMSC-testing.csv")

# Data preprocessing
# Fill missing values with mean
df_train = df_train.fillna(df_train.mean())
df_test = df_test.fillna(df_test.mean())

# Drop unnecessary columns
df_train = df_train.drop(["age"], axis=1)
df_test = df_test.drop(["age"], axis=1)
df_train = df_train.drop(df_train.columns[0], axis=1)
df_test = df_test.drop(df_test.columns[0], axis=1)
df_test = df_test.drop(df_test.columns[0], axis=1)

# Train the model
X_train = df_train.drop(columns=['SeriousDlqin2yrs'])
y_train = df_train['SeriousDlqin2yrs']
model = LogisticRegression(max_iter=1500)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'trained_model1.pkl')
