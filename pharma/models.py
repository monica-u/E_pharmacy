from django.conf import settings
from django.db import models

class med(models.Model):
    medName = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    quantity = models.PositiveIntegerField()



    def publish(self):
        self.save()

    def __str__(self):
        return self.medName