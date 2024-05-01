from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Room, Topic, Message

from .formModels import RoomForm
import time


# rooms = [
#     {'id':1, 'name':'Fortnite'},
#     {'id':2, 'name':'PUBG'},
#     {'id':3, 'name':'DB Legends'},
# ]

def logoutUser(request):
    # time.sleep(1)
    logout(request)
    # time.sleep(1)
    return redirect('home_name')
 
def loginPage(request):

    pageType = 'login'
    context={'page': pageType}

    if request.user.is_authenticated:
        return redirect('home_name')
    
    if request.method=='POST':
        curUser = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            curUser=User.objects.get(username=curUser)
        except:
            messages.error(request, "User doesn't exist")

        curUser = authenticate(request, username=curUser, password=password)

        if curUser is not None:
            login(request, curUser)
            return redirect('home_name')
        else:
            messages.error(request, "Username or Password doesn't exist")
        
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    
    form=UserCreationForm()
    pageType='register'

    context={'page': pageType, 'form': form}  

    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            curUser = form.save(commit=False)
            curUser.username = curUser.username.lower()
            curUser.save()
            login(request, curUser)
            return redirect('home_name')
        else:
            messages.error(request, "An Error during Registration")

    return render(request, 'base/login_register.html', context)

# Create your views here.
def home(request):
    query = request.GET.get('query')
    rooms=Room.objects.filter()
    if query:
        rooms=Room.objects.filter(
            Q(topic__name__icontains=query) |
            Q(name__icontains=query) |
            Q(host__username__icontains=query) |
            Q(description__icontains=query))
        
    topics=Topic.objects.all()
    context={'rooms':rooms, 'rooms_count':rooms.count(), 'topics':topics}
    return render(request, 'base/home.html', context)

# Getting pk from the url call, sending curRoom as context to the html file room.html
def room(request, pk):
    curRoom=Room.objects.get(id=pk)
    curRoom_messages=Message.objects.filter(room__id=pk).order_by('-created')
    
    context={'room':curRoom, 'userMessages':curRoom_messages}
    if request.method=='POST':
        curMessage=Message.objects.create(
            user=request.user,
            room=curRoom,
            body=request.POST.get('body')
            )
        return redirect('room_name', pk=pk) 
    
    
    return render(request, 'base/room.html', context)

@login_required(login_url='login_name')
def createRoom(request):
    curForm=RoomForm()
    if request.method=='POST':
        curForm=RoomForm(request.POST)
        if curForm.is_valid():
            curForm.save()
            return redirect('home_name')
    
    context={'form':curForm}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login_name')
def updateRoom(request, pk):
    roomToUpdate=Room.objects.get(id=pk)
    curForm=RoomForm(instance=roomToUpdate)

    if request.user != roomToUpdate.host:
        return HttpResponse("Bhaago yahan se")
    
    if request.method=='POST':
        curForm=RoomForm(request.POST, instance=roomToUpdate)
        if curForm.is_valid():
            curForm.save()
            return redirect('home_name')


    context={'form':curForm}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login_name')
def deleteRoom(request, pk):
    roomToDelete=Room.objects.get(id=pk)

    if request.user != roomToDelete.host:
        return HttpResponse("Acha Ji, Delete Karoge?")
    
    if request.method=='POST': 
        roomToDelete.delete()
        return redirect('home_name')
    context={'room':roomToDelete}
    return render(request, 'base/delete.html', context)
    #return redirect('delete-room_name')

