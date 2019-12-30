from django import forms
from .models import Playground


class PlaygroundForm(forms.ModelForm):
    class Meta:
        model = Playground
        fields = (
            'latitude',
            'longitude',
            'address',
            'playground_type',
            'description',
            'rating',
            'photo',
        )
    
    def __init__(self, *args, **kwargs):
        super(PlaygroundForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False