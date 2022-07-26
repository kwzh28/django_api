from django.db import models

# Create your models here.

class StocksInfo(models.Model):
   ## Stock_Name = models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True)
    Open = models.DecimalField(max_digits=10, decimal_places=6)
    High = models.DecimalField(max_digits=10, decimal_places=6)
    Low = models.DecimalField(max_digits=10, decimal_places=6)
    Close = models.DecimalField(max_digits=10, decimal_places=6)
    Volume = models.IntegerField()



    def __str__(self):
        return self.Date
