from django import forms
from web_registry.models import *


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('entry_type', 'value')
        #fields = ('entry_type', 'value', 'upload')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('value',)
