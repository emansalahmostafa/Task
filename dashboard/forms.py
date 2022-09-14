from dataclasses import fields
from django import forms
from .models import Inpatient

class InPatientForm(forms.ModelForm):
    class Meta:
        model = Inpatient  
        fields='__all__'
       #fields  =['name','bp','pulse','temperature','respiration','symptoms_type','symptoms_title','symptoms_description','gender'] 