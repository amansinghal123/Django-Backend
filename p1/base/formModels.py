from django.forms import ModelForm
from .models import Room, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room

        # This will create metaData fiels from the parent class Rooms. 
        fields = '__all__'
        exclude = ['host', 'participants'] 
