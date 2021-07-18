from django import forms
from .models import ContactInfo






class ContactInfoForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    desc=forms.CharField(max_length=50)
    date=forms.DateField()
    

    class Meta:
        model=ContactInfo
        fields="__all__"


