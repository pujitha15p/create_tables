from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    d={'AccessRecords':QLAO}
    return render(request,'display_accessrecords.html',d)



def insert_topic(request):
    tn=input('enter tn')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is inserted')


def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('webpage is created')

def insert_access(request):
    pk=int(input('enter pk value of webpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return HttpResponse('Access is created')