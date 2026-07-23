import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
data = pd.read_csv("student_performance.csv")

# Features and Target
X = data[['hours_studied', 'attendance', 'previous_score']]
y = data['final_score']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

# Model
# Model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "model.pkl")
print("Model saved successfully!")

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MAE:", mean_absolute_error(y_test, y_pred))