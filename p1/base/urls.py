from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_name"),

    # Calls the view --> room for the link /room/anything, and anything is sent to the function views.room as an parameter
    path('room_page/<str:pk>/', views.room, name="room_name"),
    path('create-room/', views.createRoom, name="create-room_name"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room_name"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room_name"),
]