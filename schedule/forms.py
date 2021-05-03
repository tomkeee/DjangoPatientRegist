from django import forms
from doctor.models import Doctor
from django.forms import ModelForm
from .models import Booking
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput



class BookingForm(forms.ModelForm):
    
    class Meta:
        model=Booking
        fields=["user","doctor","check_in_date","check_out_date"]
        # fields=["doctor","check_in_date","check_out_date"]

        widgets={
            "user":forms.Select(attrs={'class':'form-control'}) ,
            "doctor":forms.Select(attrs={'class':'form-control'}),
            "check_in_date":DateTimePickerInput(format='%Y-%m-%d %H:%M'),
            "check_out_date":DateTimePickerInput(format='%Y-%m-%d %H:%M')
        }

        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            self.fields['check_in_date'].input_formats=(settings.DATE_INPUT_FORMATS)
            self.fields['check_out_date'].input_formats=(settings.DATE_INPUT_FORMATS)  
            self.fields['check_in_date'].widget.format = '%d-%m-%Y %H:%M:%S'
            self.fields['check_out_date'].widget.format = '%d-%m-%Y %H:%M:%S'
