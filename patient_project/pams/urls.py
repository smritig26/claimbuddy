from django.urls import path
from .views import patient_list, add_patient

urlpatterns = [
    path('', patient_list, name='patient-list'),
    path('add/', add_patient, name='add-patient'),
]
