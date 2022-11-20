from email.policy import default
from django.db import models
# Create your models here.
class RealTimeBigData(models.Model):
    appname=models.CharField(max_length=200)
    url=models.CharField(max_length=2056)
    online=models.BooleanField(default=False)
    code=models.IntegerField(null=True,blank=True)
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
    code=models.IntegerField(null=True,blank=True)
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.appname
    class Meta:
        ordering=['-date','online','appname']

class Visitor(models.Model):
    ip=models.CharField(blank=False,null=False,max_length=45)
    device_type=models.CharField(blank=False,null=True,max_length=10)
    device_name=models.CharField(blank=True,null=True,max_length=125)
    device_OS=models.CharField(blank=True,null=True,max_length=125)
    browser=models.CharField(blank=True,null=True,max_length=125)
    date=models.DateTimeField(auto_now_add=True)
