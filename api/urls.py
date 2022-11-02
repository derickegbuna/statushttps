from unicodedata import name
from django import views
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('',views.home,name='home'),
    path('<str:pk>/history/',views.statushistory,name='history'),
    path('api/',views.api,name='overview'),
    path('api/app-list/',views.applist,name='app-list'),
    path('api/live-data/',views.livedata,name='live-data'),
    path('api/app-detail/<str:pk>/',views.appdetail,name='app-detail'),
    path('api/update/',views.updatestatus,name='update'),
]

urlpatterns=format_suffix_patterns(urlpatterns)