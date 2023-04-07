from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

def insertTopic(request):

    Tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=Tn)[0]
    TO.save()

    return HttpResponse('insertion successful')

def insertWebpage(request):

    tn=input('enter topic_name:')

    n=input('enter name:')
    u=input('enter url:')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    return HttpResponse('insertion successful')


def insertAccessRecord(request):

    tn=input('enter topic_name:')
    n=input('enter name:')
    u=input('enter url:')
    an=input('enter author:')
    dt=input('enter dt:')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    
    
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    

    AO=AccessRecord.objects.get_or_create(name=WO,author=an,date=dt)[0]  
    AO.save()

    return HttpResponse('insertion successful')
    

