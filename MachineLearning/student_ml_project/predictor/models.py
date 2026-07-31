from django.db import models

class Prediction(models.Model):

    name = models.CharField(max_length=100, default="Student")

    hours_studied = models.FloatField()

    attendance = models.FloatField()

    previous_score = models.FloatField()

    predicted_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name