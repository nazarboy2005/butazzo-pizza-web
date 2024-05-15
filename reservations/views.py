from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reservations.forms import ReservationsModelForm


class ReservationsModelView(CreateView):
    template_name = 'reservation.html'
    form_class = ReservationsModelForm

    def get_success_url(self):
        return reverse_lazy('reservations:reservation')

    def form_valid(self, form):
        reservation = form.save(commit=False)
        data = form.cleaned_data

        date = str(data.get("date")).split('-')[::-1]
        joined_date = '-'.join(date)

        formatted_date = datetime.strptime(joined_date, '%d-%m-%Y').date()
        reservation.date = formatted_date

        time = str(data.get('time'))
        print("Time before parsing:", time)
        time_format = '%I:%M %p'
        formatted_time = datetime.strptime(time, time_format)
        reservation.time = formatted_time.time()

        reservation.save()
        return render(self.request, 'success.html')
        # return super().form_valid(form)


    def form_invalid(self, form):
        return render(self.request, 'form-errors.html', context={'error': form.errors})
