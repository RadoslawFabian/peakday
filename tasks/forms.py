from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Short description', 'rows': 2}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})  # Pole typu "time"
        }
