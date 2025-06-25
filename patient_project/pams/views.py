from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'pams/patient_list.html', {'patients': patients})


# from django.shortcuts import render, redirect
# from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-list')
    else:
        form = PatientForm()
    
    return render(request, 'pams/add_patient.html', {'form': form})
