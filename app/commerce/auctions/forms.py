from .models import *
from django import forms


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

