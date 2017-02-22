from .models import RegisterDesk
from django import forms



class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterDesk
        fields = ['candidate_name', 'candidate_college', 'candidate_email', 'candidate_contact_no', 'events_enrolling']

