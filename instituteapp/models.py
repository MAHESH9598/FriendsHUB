from django.db import models

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    ratig=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=1000)