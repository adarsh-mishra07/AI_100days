from django.shortcuts import render
import pandas as pd
import joblib
from .models import Prediction

# Load model only once
model = joblib.load("model.pkl")


def home(request):

    prediction = None

    if request.method == "POST":
        name = request.POST["name"]
        hours = float(request.POST["hours"])
        attendance = float(request.POST["attendance"])
        previous_score = float(request.POST["previous_score"])

        student = pd.DataFrame({
            "hours_studied": [hours],
            "attendance": [attendance],
            "previous_score": [previous_score]
        })

        # ML Prediction
        prediction = model.predict(student)[0]
        prediction = round(prediction, 2)

        # Save in Database
        Prediction.objects.create(
    name=name,
    hours_studied=hours,
    attendance=attendance,
    previous_score=previous_score,
    predicted_score=prediction
)
    predictions = Prediction.objects.all().order_by("-created_at")
    return render(
    request,
    "home.html",
    {
        "prediction": prediction,
        "predictions": predictions
    }
)