from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import Http404,HttpResponseRedirect
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def patient_list_view(request):
    queryset=Patient.objects.all()
    context = {
        "content":queryset
    }
    return render(request,"patient/patient_list.html",context)

@staff_member_required
def patient_create_view(request):
    if request.method=="POST":
        form=PatientForm(request.POST or None)

        if form.is_valid:
            form.save()
            form=PatientForm()
        return HttpResponseRedirect("/")
    else:
        form=PatientForm()
    context={"form":form}
    return render(request,"patient/create_form.html",context)

def patient_detail_view(request,pk):
    try:
        obj=Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        raise Http404
    if request.method=="POST":
        obj.delete()
        return render(request,"patient/patient_delete_success.html",{})
    context={"object":obj}
    return render(request,"patient/patient_detail.html",context)