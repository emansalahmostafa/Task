from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from .models import Inpatient
from .forms import InPatientForm



@login_required
def index(request):
    inpatients= Inpatient.objects.all()
    inpatients_count = inpatients.count()

    


    
    context={
        'inpatients':inpatients,
        'inpatients_count': inpatients_count,
    }
    return render(request, 'dashboard/index.html',context)



@login_required
def inpatient(request):
    inpatients= Inpatient.objects.all()
   # inpatients= Inpatient.objects.raw('SELECT * FROM dashboard_inpatient')
    context={
        'inpatients':inpatients,

    }
    
    return render(request, 'dashboard/inpatient.html',context)


def inpatient_delete(request, pk):
    inpatients = Inpatient.objects.get(id=pk)
    if request.method == 'POST':
        inpatients.delete()
        return redirect('dashboard-inpatient')
    context = {
        'inpatients': inpatients
    }
    return render(request, 'dashboard/inpatient_delete.html', context)


#def inpatient_edit(request, pk):
    inpatients = Inpatient.objects.get(id=pk)
    if request.method == 'POST':
        form = InPatientForm(request.POST, instance=inpatients)
        if form.is_valid():
            form.save()
            return redirect('dashboard-inpatient-form')
    else:
        form = InPatientForm(instance=inpatients)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/inpatient_edit.html', context)



class AddPatientView(CreateView):
    model = Inpatient
    form_class = InPatientForm
    success_url = reverse_lazy("dashboard-inpatient")
    template_name = 'dashboard/form.html'