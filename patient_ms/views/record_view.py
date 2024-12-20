import logging
from datetime import datetime
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib import messages
from django.urls import reverse_lazy
from patient_ms.models import (
    DoctorPrescription,
    Patient,
    DoctorAppointment
)
from patient_ms.views.get_pdf import render_pdf

logger = logging.getLogger(__name__)


class ViewAllSavedRecord(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    template_name = 'dashboard/record/record_view.html'
    model = DoctorPrescription

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request, pk):
        appointment = DoctorAppointment.objects.get(pk=pk)
        try:
            patient_data = appointment.patient.patient_data
        except Exception as e:
            logger.info(f"{'*' * 10} e: {e}\n")
            patient_data = None

        objects_list = self.model.objects.filter(
            appointment=appointment,
            patient=patient_data
        ).order_by('-created_at')
        context = {
            "objects_list": objects_list,
            "patient": patient_data
        }
        return render(request, self.template_name, context)


class PMSViewAllSavedRecord(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    template_name = 'dashboard/record/pms_record_view.html'
    model = DoctorPrescription

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request, pk):
        appointment = DoctorAppointment.objects.get(pk=pk)
        try:
            patient_data = appointment.patient.patient_data
        except Exception as e:
            logger.info(f"{'*' * 10} e: {e}\n")
            patient_data = None

        objects_list = self.model.objects.filter(
            appointment=appointment,
            patient=patient_data
        ).order_by('-created_at')
        context = {
            "objects_list": objects_list,
            "patient": patient_data
        }
        return render(request, self.template_name, context)


class ViewAllDownloadRecord(UserPassesTestMixin, LoginRequiredMixin, View):
    template_name = 'dashboard/record/record_view_pdf.html'
    model = DoctorPrescription

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request, pk):
        prescription_pk = request.GET.get('prescription_pk')
        prescription = self.model.objects.filter(pk=prescription_pk).first()
        try:
            patient_data = prescription.patient
        except Exception as e:
            logger.info(f"{'*' * 10} e: {e}\n")
            patient_data = None

        today_date = datetime.today().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD
        file_name = f"prescription_copy-{prescription.pk}-{today_date}"

        context = {
            "object": prescription,
            "patient": patient_data
        }
        return render_pdf(request, self.template_name, context, file_name)
