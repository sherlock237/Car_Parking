from django.db import models
from datetime import datetime
# Create your models here.
class park(models.Model):
    id=models.AutoField(primary_key=True)
    car_number=models.CharField(max_length=100)
    time_in=models.DateTimeField(default=datetime.now())
    car_slot=models.IntegerField()
    def __str__(self):
        return self.car_number+" "+str(self.car_slot)

   