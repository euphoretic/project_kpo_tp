from django import forms
from django.core.exceptions import ValidationError

from wander.models import Poster, Places


class EventForm(forms.ModelForm):
    class Meta:
        model = Poster
