from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from patient_ms.models import DoctorAppointment



class DoctorAppointmentForm(forms.ModelForm):
    class Meta:
        model = DoctorAppointment
        exclude = [
            'patient',
            "serial_number",
            "is_visited",
            'appointment_close_time',
            'status'
        ]
        widgets = {
            'division': forms.Select(attrs={
                'id': 'division'
            }),
            'district': forms.Select(attrs={
                'id': 'district'
            }),
            'upazila': forms.Select(attrs={
                'id': 'upazila'
            }),
            'appointment_day': forms.DateInput(
                attrs={
                    'type': 'date'
                }),
            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                })
        }

    def __init__(self, *args, **kwargs):
        super(DoctorAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].required = True
        self.fields['appointment_day'].required = True
        self.fields['appointment_time'].required = True
        self.fields['speciality'].required = True

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        today = timezone.now().date()
        doctor_daily_limit = doctor.daily_appointment_limit
        # max limit per day
        today_appointed_count = DoctorAppointment.objects.filter(
            created_at=today, doctor=doctor
        ).count()

        if today_appointed_count >= doctor_daily_limit:
            raise ValidationError(
                "Daily appointment limit reached for this doctor. \
                    Please try other days"
            )

        return cleaned_data
