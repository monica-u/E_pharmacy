from django.db import models

class Prescription(models.Model):
    message = models.CharField(max_length=200)
