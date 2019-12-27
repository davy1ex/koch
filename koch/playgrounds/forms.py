from django import forms
from .models import Playground


class PlaygroundForm(forms.ModelForm):
    class Meta:
        model = Playground
        fields = (
            'latitude',
            'longitude',
            'playground_type',
            'description',
            'photo',            
        )