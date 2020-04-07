from django import forms
from .models import Prescription
from accounts.models import Doctor


class TimeInput(forms.TimeInput):
    input_type = 'time'


class treatPatientForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = ['remarks']


class takeAppointmentForm(forms.Form):

    time = forms.TimeField(widget=TimeInput(), required=True)
    specialization = forms.ChoiceField(choices=Doctor.SPECIALIZATION_CHOICES)
