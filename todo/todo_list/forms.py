from django.contrib.auth.models import User
from django import forms
from models import Task
from django.forms.extras.widgets import SelectDateWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class AddListForm(forms.Form):
    listname = forms.CharField(max_length=200)
    
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': SelectDateWidget,
        }