from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',d)
def display_Webpage(request):
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.filter(name='raji')
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('-name'))
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_Webpage.html',d)
def Access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'Access.html',d)
def update_Webpage(request):
    Webpage.objects.filter(name='raji').update(url='https://raji.in')
    Webpage.objects.filter(name='sow').update(mail='sow12@gmail.com')
    Webpage.objects.filter(topic_name='football').update(name='malli')
    Webpage.objects.update_or_create(name='vasu',defaults={'mail':'vasu2@gmail.com'})
    to=Topic.objects.get_or_create(topic_name='hoky')[0]
    to.save()
    Webpage.objects.update_or_create(name='kasu',defaults={'topic_name':to,'url':'https://kasu','mail':'kasu@gmail.com'})
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_Webpage.html',d)
def delete_Webpage(request):
    #Webpage.objects.filter(name='thanu').delete()
    Webpage.objects.all().delete()
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_Webpage.html',d)