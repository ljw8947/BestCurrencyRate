from django.db import models
from datetime import datetime
# Create your models here.
class CurrencyRate(models.Model):
    rateID=models.IntegerField(primary_key=True)
    sourceCode=models.CharField(max_length=10)
    currencyCode=models.CharField(max_length=3)
    sellPrice=models.DecimalField(decimal_places=6,max_digits=15)
    buyPrice=models.DecimalField(decimal_places=6,max_digits=15)
    date=models.DateTimeField(default=datetime.now)
    createTime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "rateid:%d souceCode:%s currencyCode:%s sellPrice:%d buyPrice:%d date:%s createTime:%s" % \
            (self.rateID,self.sourceCode,self.currencyCode,self.sellPrice,self.buyPrice,self.date,self.createTime)
