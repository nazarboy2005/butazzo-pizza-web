from django import forms

from reservations.models import ReservationsModel


class ReservationsModelForm(forms.ModelForm):

    class Meta:
        model = ReservationsModel
        fields = ['full_name', 'email', 'phone_number', 'date', 'time', 'message']
