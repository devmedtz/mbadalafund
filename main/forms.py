from django import forms
from .models import *


class PitchForm(forms.ModelForm):

    class Meta:
        model = Pitch
        fields = '__all__'