from django.shortcuts import render
from django.http import HttpResponse
from . models import Room


# rooms =[
#     {'id':1, 'name':'Kifaru'},
#     {'id':2, 'name':'Nyati'},
#     {'id':3, 'name':'Ndovu'},
#     {'id':4, 'name':'Simba'},
#     {'id':5, 'name':'Chui'},
# ]

def home(request):
    rooms = Room.objects.all()
    context ={'rooms':rooms}
    return render(request, "home.html",context)

def room(request,pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)
    context ={'room':room}
    return render(request,'room.html',context)

def about(request):
    return render(request, "About.html")



def contact(request):
    return render(request, "contact.html")
def login(request):
    return render(request, "login.html")


# Create your views here.
