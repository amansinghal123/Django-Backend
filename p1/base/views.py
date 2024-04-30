from django.shortcuts import render, redirect

from .models import Room, Topic

from .formModels import RoomForm 

# rooms = [
#     {'id':1, 'name':'Fortnite'},
#     {'id':2, 'name':'PUBG'},
#     {'id':3, 'name':'DB Legends'},
# ]

# Create your views here.
def home(request):
    query = request.GET.get('query')
    rooms=Room.objects.filter()
    if query:
        rooms=Room.objects.filter(topic__name__icontains=query)
    topics=Topic.objects.all()
    context={'rooms':rooms, 'topics':topics}
    return render(request, 'base/home.html', context)

# Getting pk from the url call, sending curRoom as context to the html file room.html
def room(request, pk):
    curRoom=Room.objects.get(id=pk)
    context={'room':curRoom}
    return render(request, 'base/room.html', context)

def createRoom(request):
    curForm=RoomForm()
    if request.method=='POST':
        curForm=RoomForm(request.POST)
        if curForm.is_valid():
            curForm.save()
            return redirect('home_name')
    
    context={'form':curForm}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    roomToUpdate=Room.objects.get(id=pk)
    curForm=RoomForm(instance=roomToUpdate)

    if request.method=='POST':
        curForm=RoomForm(request.POST, instance=roomToUpdate)
        if curForm.is_valid():
            curForm.save()
            return redirect('home_name')


    context={'form':curForm}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    roomToDelete=Room.objects.get(id=pk)
    if request.method=='POST': 
        roomToDelete.delete()
        return redirect('home_name')
    context={'room':roomToDelete}
    return render(request, 'base/delete.html', context)
    #return redirect('delete-room_name')