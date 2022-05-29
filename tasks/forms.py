from django.forms import DateTimeInput, Select, ModelForm, TextInput
from .models import Task

class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'deadline']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'deadline': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }