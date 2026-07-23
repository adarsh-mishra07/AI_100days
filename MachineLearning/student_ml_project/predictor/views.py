from django.shortcuts import render
import pandas as pd
import joblib

# Load model only once
model = joblib.load("model.pkl")


def home(request):

    prediction = None

    if request.method == "POST":

        hours = float(request.POST["hours"])
        attendance = float(request.POST["attendance"])
        previous_score = float(request.POST["previous_score"])

        student = pd.DataFrame({
            "hours_studied": [hours],
            "attendance": [attendance],
            "previous_score": [previous_score]
        })

        prediction = model.predict(student)[0]

        prediction = round(prediction, 2)

    return render(
        request,
        "home.html",
        {"prediction": prediction}
    )