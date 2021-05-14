from django.shortcuts import render, redirect
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
            form.save()
            form=BookingForm()
        return redirect("/")
    else:
        form=BookingForm()
    context={"my_form":form}
    return render(request,"schedule/create_form.html",context)

def booking_list_view(request):
    queryset=Booking.objects.all()
    context={
        "content":queryset
    }
    return render(request,"schedule/booking_list.html",context)