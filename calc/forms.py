from django import forms
from .models import UserData


class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('electricity_current', 'electricity_past', 'electricity_tariff',  'water_current', 'water_past',
                  'water_tariff')
