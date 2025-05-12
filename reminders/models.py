from django.db import models

class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    reminder_date = models.DateField()
    reminder_time = models.TimeField()

     
