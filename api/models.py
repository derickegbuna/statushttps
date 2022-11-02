from email.policy import default
from django.db import models
# Create your models here.
class RealTimeBigData(models.Model):
    appname=models.CharField(max_length=200)
    url=models.CharField(max_length=2056)
    online=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.appname
    class Meta:
        ordering=['-created','appname']

class MostUsedApp(models.Model):
    appname=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    parent_company=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.appname
    class Meta:
        ordering=['parent_company']


class LiveData(models.Model):
    appname=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    online=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.appname
    class Meta:
        ordering=['online','appname']

