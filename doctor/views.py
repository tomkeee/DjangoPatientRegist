from django.shortcuts import render,redirect
from .models import Doctor
from .forms import DoctorForm

# Create your views here.
def doctor_list_view(request):
    queryset=Doctor.objects.all()
    context = {
        "content":queryset
    }
    return render(request,"doctor/doctor_list.html",context)

def doctor_detail_view(request,pk):
    try:
        obj=Doctor.objects.get(id=pk)
    except Patient.DoesNotExist:
        raise Http404
    if request.method=="POST":
         obj.delete()
         return redirect("/doctors")
    context={
        "object":obj
    }
    return render(request,"doctor/doctor_detail.html",context)

def doctor_create_view(request):
    if request.method=="POST":
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            form=DoctorForm()
        return redirect("/doctor")
    else:
        form=DoctorForm()
    context={"form":form}
    return render(request,"doctor/create_form.html",context)