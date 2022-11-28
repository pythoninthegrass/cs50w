#!/usr/bin/env python3

from django import forms
from .models import MarkedDownExample


class MarkedDownExampleForm(forms.ModelForm):
    class Meta:
        model = MarkedDownExample
        fields = '__all__'
