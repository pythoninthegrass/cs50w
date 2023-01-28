from .models import *
from . import util
from django import forms


class MarkdownForm(forms.ModelForm):
    class Meta:
        model = Markdown
        fields = '__all__'

    # TODO: remove single bullet point validation error message
    def clean(self):
        super(MarkdownForm, self).clean()
        title = self.cleaned_data.get('title')

        if util.search_entries(title) is not None:
            raise forms.ValidationError({'title': 'Entry already exists.'})


class MarkdownEditForm(forms.ModelForm):
    class Meta:
        model = Markdown
        fields = '__all__'
