from django import forms
from service_requests.models import ServiceRequest

class UpdateRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'resolved_at']
        widgets = {
            'resolved_at': forms.DateInput(attrs={'type': 'date'}),
        }
