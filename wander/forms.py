from django import forms
from django.core.exceptions import ValidationError

from wander.models import PosterEvent, Place


class EventForm(forms.ModelForm):
    class Meta:
        model = PosterEvent


class SearchForm(forms.Form):
    q = forms.CharField()
    c = forms.ModelChoiceField(
        queryset=PosterEvent.objects.all().order_by('name'))

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
