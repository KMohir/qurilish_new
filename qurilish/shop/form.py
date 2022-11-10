from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import City, Category, Product


class findForm(forms.Form):
    class Meta:
        model=Product


    city=forms.ModelChoiceField(queryset=City.objects.all(),to_field_name='slug',required=False,
                                    widget=forms.Select(attrs={'class':'form-select'}))
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),to_field_name='slug',required=False
                                      ,widget=forms.CheckboxSelectMultiple)
