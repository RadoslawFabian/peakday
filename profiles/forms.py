from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'location', 'birth_date', 'weight', 'height']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Describe yourself...'
        })
        self.fields['location'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your location'
        })
        self.fields['profile_picture'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['weight'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your weight in kg'
        })
        self.fields['height'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your height in cm'
        })
