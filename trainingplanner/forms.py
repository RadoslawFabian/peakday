from django import forms
from django.forms import inlineformset_factory
from .models import Training, Exercise

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name']

ExerciseFormSet = inlineformset_factory(Training, Exercise,
                                        fields=('name', 'sets', 'reps'),
                                        extra=1,
                                        can_delete=True)
