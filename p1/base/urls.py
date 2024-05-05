from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_name"),

    # Calls the view --> room for the link /room/anything, and anything is sent to the function views.room as an parameter
    path('room_page/<str:pk>/', views.room, name="room_name"),
    path('create-room/', views.createRoom, name="create-room_name"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room_name"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room_name"),

    path('login/', views.loginPage, name="login_name"),
    path('logout/', views.logoutUser, name="logout_name"),
    path('register/', views.registerPage, name="register_name"),

    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message_name"),
    path('edit-message/<str:pk>', views.editMessage, name="edit-message_name"),

    path('user_profile/<str:pk>/', views.userProfile, name="userProfile_name"),
    path('update_user_profile/<str:pk>/', views.updateUserProfile, name="updateUserProfile_name"),

    path('topics/', views.topicsPage, name="topics_name"),
    path('activity/', views.activityPage, name="activity_name"),

    path('request-topic/', views.requestTopic, name="requestTopic_name"),
]