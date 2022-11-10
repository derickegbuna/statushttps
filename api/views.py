from collections import defaultdict
from email import header
from itertools import cycle
from multiprocessing import context
from threading import Thread
from time import sleep
from turtle import done
from unicodedata import name
from urllib import response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import RealTimeBigData, MostUsedApp, LiveData
from .serializer import RealTimeBigDataSerializer,MostUsedAppSerializer,LiveDataSerializer
from api import serializer
import requests
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# NOTEs
# NB: TIKTOK response.status_code returns 403
# NB: UBER response.status_code returns 406
# NB: https://api.whatsapp.com response.status_code 400 when headers is added to the get request but returns 200 without headers
# To solve the above problem we have to add Header to the GET
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # TO CHECK which App is UP or DOWN
def is_SERVER_up(url):
    try:
        #headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
        headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return True
        else:
            error_code=response.status_code
            return False, error_code
    except requests.exceptions.RequestException as e:
        return e
# Create your views here.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WEBSITE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@api_view(['GET'])
def home(request):
    data=LiveData.objects.all()
    recent=data[:1]
    context={
        'app':data,
        'update':recent,
    }
    return render(request,'api.html',context)

@api_view(['GET'])
def statushistory(request,pk):
    data=RealTimeBigData.objects.filter(appname=pk)
    context={
        'data':data,
        'appname':pk,
    }
    return render(request,'app.html',context)

@api_view(['GET'])
def about_us(request):
    context={}
    return render(request, 'aboutus.html', context)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ALL THE SOCIAL APPs AND ALL THEIR UPTIME AND DOWNTIME 
@api_view(['GET'])
def applist(request,format=None):
    try:
        app=RealTimeBigData.objects.all()
    except RealTimeBigData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=RealTimeBigDataSerializer(app,many=True)
    return Response(serializer.data)

# ALL THE SOCIAL APPs AND MOST RECENT STATES OF THIER SERVERS
@api_view(['GET'])
def livedata(request):
    try:
        app=LiveData.objects.all()
    except LiveData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=LiveDataSerializer(app,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def appdetail(request,pk,format=None):
    try:
        app=RealTimeBigData.objects.filter(appname=pk)
    except RealTimeBigData.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    serializer=RealTimeBigDataSerializer(app,many=True)
    return Response(serializer.data)

# UPDATE LIVE STATUS
# This will be run at a particular time interval.
@api_view(['PUT'])
def updatestatus(request):
    app=LiveData.objects.all()
    appname=app.values_list('appname','url','online')
    for i in appname:
        print('================================================')
        print(f'Checking {i[0]} Server....')
        status=is_SERVER_up(i[1])
        if status:
            stat='Online'
            data={'appname':i[0],'url':i[1],'online':status,'code':200}
            RealTimeBigData.objects.create(appname=i[0],url=i[1],online=status,code=200)
            if i[2]!=status:
                app=LiveData.objects.get(appname=i[0])
                serializer=LiveDataSerializer(app,data=data)
                if serializer.is_valid():
                    serializer.save()
        else:
            stat='Offline'
            online=status[0]
            code=status[1]
            data={'appname':i[0],'url':i[1],'online':online,'code':code}
            RealTimeBigData.objects.create(appname=i[0],url=i[1],online=online,code=code)
            if i[2]!=online:
                app=LiveData.objects.get(appname=i[0])
                serializer=LiveDataSerializer(app,data=data)
                if serializer.is_valid():
                    serializer.save()
        print(f'{i[0]} Server is {stat}' )
    return Response("Server Data Updated")