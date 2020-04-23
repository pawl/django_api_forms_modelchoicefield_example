from django import forms
from django_api_forms import Form, FormFieldList

from . import models


class SongForm(Form):
    title = forms.CharField(required=True, max_length=100)
    artist = forms.ModelChoiceField(queryset=models.Artist.objects.all())


class PlaylistForm(Form):
    songs = FormFieldList(form=SongForm)
