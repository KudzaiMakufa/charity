from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from donation.models import Donation 

# model form 
from django.db import models
# from django.forms import ModelForm , Textarea , ModelChoiceField , Select  


class Donation_Form(forms.ModelForm):
    class Meta:
        model = Donation
  
        
        fields = ['name','donation_details' ,'amount','beneficiaries','purpose']

             
        widgets = {
            'purpose': forms.TextInput(attrs={
                "type" : "text",
                "class":"form-control"
            }),
            'donation_details': forms.Textarea(attrs={
              
                "rows":10,
                "class":"form-control"
            }),
            'beneficiaries': forms.Textarea(attrs={
                "rows":5,
                "class":"form-control"
            }),
            'amount': forms.TextInput(attrs={
                "type" : "text",
                "class":"form-control"
            }),
            'name': forms.Select(attrs={
                "class":"form-control custom-select"
            }),
           
        }