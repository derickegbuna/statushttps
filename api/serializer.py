from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import RealTimeBigData,MostUsedApp,LiveData
from django.contrib.humanize.templatetags.humanize import naturaltime

class RealTimeBigDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=RealTimeBigData
        fields=['appname','url','online','created']
    def to_representation(self, instance):
        representation=super(RealTimeBigDataSerializer, self).to_representation(instance)
        representation['created']=naturaltime(instance.created)
        return representation

class MostUsedAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=MostUsedApp
        fields=['appname','url']


class LiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=LiveData
        fields=['appname','url','online','date']
    def to_representation(self, instance):
        representation=super(LiveDataSerializer,self).to_representation(instance)
        representation['date']=naturaltime(instance.date)
        return representation
    
# class TestingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=RealTimeData
#         fields='__all__'
#     def to_representation(self, instance):
#         representation=super(RealTimeDataSerializer,self).to_representation(instance)
#         representation['date']=naturaltime(instance.date)
#         return representation



# Canva pro
# pixellab
# hbo max
# boom play
# disney+
# grammarly
# shazam
# amazon prime
# apple music