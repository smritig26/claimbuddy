from django.core.management.base import BaseCommand
from pams.models import Patient

class Command(BaseCommand):
    help = 'Seed the database with dummy patient data'

    def handle(self, *args, **kwargs):
        data = [
            {"full_name": "John Doe", "age": 30, "gender": "M", "insurance_provider": "HDFC", "policy_number": "H123"},
            {"full_name": "Jane Smith", "age": 25, "gender": "F", "insurance_provider": "LIC", "policy_number": "L456"},
            {"full_name": "Alice Johnson", "age": 40, "gender": "F", "insurance_provider": "Tata AIG", "policy_number": "T789"},
            {"full_name": "Bob Brown", "age": 50, "gender": "M", "insurance_provider": "ICICI", "policy_number": "I321"},
            {"full_name": "Charlie", "age": 35, "gender": "O", "insurance_provider": "Max Bupa", "policy_number": "M654"},
        ]

        for patient in data:
            Patient.objects.get_or_create(**patient)

        self.stdout.write(self.style.SUCCESS("✅ Dummy data added successfully."))
