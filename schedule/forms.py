from django import forms
from doctor.models import Doctor
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
            "check_in_date":DateTimePickerInput(format='%d-%m-%Y %H:%M'),           
            "check_out_date":DateTimePickerInput(format='%d-%m-%Y %H:%M'),           
        }

# class BookingForm(forms.Form):
#     doctor= forms.ChoiceField(choices='doctor'),
#     check_in_date=forms.DateTimeField(widget=DateTimePickerInput(format='%d/%m/%Y'))
#     check_in_time=forms.DateTimeField(widget=DateTimePickerInput(format='%H:%M'))
#     check_out_date=forms.DateTimeField(widget=DateTimePickerInput(format='%d/%m/%Y'))
#     check_out_time=forms.DateTimeField(widget=DateTimePickerInput(format='%H:%M'))

