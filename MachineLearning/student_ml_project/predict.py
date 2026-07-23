import pandas as pd
import joblib

model = joblib.load("model.pkl")

new_student = pd.DataFrame({
    "hours_studied": [6],
    "attendance": [85],
    "previous_score": [72]
})

prediction = model.predict(new_student)

print("Predicted Final Score:", prediction[0])