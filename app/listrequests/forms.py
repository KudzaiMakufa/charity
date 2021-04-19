from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from listrequests.models import Charity_Request 

# model form 
from django.db import models
# from django.forms import ModelForm , Textarea , ModelChoiceField , Select  


class Charity_Request_Form(forms.ModelForm):
    confirm_password = forms.CharField(required=False , widget= forms.PasswordInput(
    attrs={
    
        "class":"form-control",
  
    }
    ))

    class Meta:
       
        model = Charity_Request
  

        fields = ['organisation_name','address' ,'phone', 'email','constitution_doc','deeds_document','elligibility_doc','charity_type','password']

             
        widgets = {
            
            'organisation_name': forms.TextInput(attrs={
                "type" : "text",
                "class":"form-control"
            }),
            'address': forms.TextInput(attrs={
                "type" : "text",
                "class":"form-control"
            }),
            'phone': forms.TextInput(attrs={
                "type" : "text",
                "class":"form-control"
            }),
            'email': forms.TextInput(attrs={
                "type" : "email",
                "class":"form-control"
            }),

            'deeds_document': forms.ClearableFileInput(attrs={
                "class":"form-control",
                "id":"deeds_document",
                "type" : "file",
            }),
            'elligibility_doc': forms.ClearableFileInput(attrs={
                "class":"form-control",
                "id":"elligibility_doc",
                "type" : "file",
            }),
            'constitution_doc': forms.ClearableFileInput(attrs={
                "class":"form-control",
                "id":"constitution_doc",
                "type" : "file",
            }),

            'charity_type': forms.Select(attrs={
                "type" : "text",
                "class":"form-control custom-select",
                "id":"charity_type"
            }),

            'password': forms.PasswordInput(attrs={
       
                "class":"form-control custom-select",
                "id":"password"
            })
           
        }