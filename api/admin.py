from django.contrib import admin
from .models import RealTimeBigData,MostUsedApp,LiveData,Visitor
# Register your models here.
# admin.site.register(RealTimeBigData)
@admin.register(RealTimeBigData)
class RealTimeBigDataAdmin(admin.ModelAdmin):
    list_display=['appname','url','online','code','created']

@admin.register(MostUsedApp)
class MostUsedAppAdmin(admin.ModelAdmin):
    list_display=['appname','url','parent_company']

@admin.register(LiveData)
class LiveDataAdmin(admin.ModelAdmin):
    list_display=['appname','url','date','online','code']

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display=['ip','device_type','device_name','device_OS','browser','date']