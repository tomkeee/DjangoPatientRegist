from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from django.contrib.auth import get_user_model
from .models import Booking

User=get_user_model()
# Create your views here.
def booking_create_view(request):
    if request.method=="POST":
        form=BookingForm(request.POST or None)
        if form.is_valid():
            user=User
            form.save()
            form=BookingForm()
        return HttpResponseRedirect("/")
    else:
        form=BookingForm()
    context={"form":form}
    return render(request,"patient/create_form.html",context)