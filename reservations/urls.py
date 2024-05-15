from django.urls import path

from reservations.views import ReservationsModelView

app_name = 'reservation'

urlpatterns = [
    path('', ReservationsModelView.as_view(), name='reservation')
]
