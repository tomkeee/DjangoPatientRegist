from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=["first_name","last_name","street","city","number","phone_number","title","price_for_visit"]
        widgets ={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'street': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'number': forms.NumberInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.Select(attrs={'class':'form-control'}),
            'price_for_visit': forms.NumberInput(attrs={'class':'form-control'}),
        } 