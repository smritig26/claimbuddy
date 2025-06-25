from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'age', 'gender', 'insurance_provider', 'policy_number']
        widgets = {
            'gender': forms.Select(choices=Patient.GENDER_CHOICES, attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'insurance_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
