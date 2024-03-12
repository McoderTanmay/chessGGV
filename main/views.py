from django.shortcuts import render
from .models import Member, Presedent, Images, Event, Contact, Resources
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name = name, email = email, phone = phone, desc = description, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, "contact.html")

def team(request):
    presedent = Presedent.objects.all()
    members = Member.objects.all()

    return render(request,"team.html",{
        'presedents' : presedent,
        'members' : members 
    })

def images(request):
    images = Images.objects.all()
    return render(request,"gallary.html",{
        "images":images
    })

def events(request):
    events = Event.objects.all()
    return render(request,'events.html',{
        "events":events
    })

def resources(request):
    resources = Resources.objects.all()
    return render(request,"resources.html",{
        "resources":resources
    })