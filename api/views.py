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

# from django.core.exceptions import ObjectDoesNotExist

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
            # return response.status_code
            return False
    except requests.exceptions.RequestException as e:
        # return response.status_code
        return False

# Create your views here.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WEBSITE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@api_view(['GET'])
def home(request):
    data=LiveData.objects.all()
    context={
        'app':data,
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
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@api_view(['GET'])
def api(request,format=None):
    test={
        '1st Step':'SignUP and Login Page',
        '2nd Step':'Redirect to "applist"',
        '3rd Step':'We will have signup and login on this page',
        '4th Step':'if login or signup is valid, redirect to livedata'
    }
    return Response(test)

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
# This will be run every interval
@api_view(['PUT'])
def updatestatus(request):
    app=LiveData.objects.all()
    appname=app.values_list('appname','url','online')
    for i in appname:
        print('-----------------------------------------------')
        print('-----------------------------------------------')
        print(f'Checking {i[0]} Server....')
        status=is_SERVER_up(i[1])
        if status:
            stat='Online'
        else:
            stat='Offline'
        print(f'{i[0]} Server is {stat}' )
        data={'appname':i[0],'url':i[1],'online':status}
        RealTimeBigData.objects.create(appname=i[0],url=i[1],online=status)
        if i[2]!=status:
            app=LiveData.objects.get(appname=i[0])
            serializer=LiveDataSerializer(app,data=data)
            if serializer.is_valid():
                serializer.save()
    return Response("Server Data Updated")