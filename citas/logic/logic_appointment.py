from measurements.models import Measurement
from ..models import Appointment

def get_appointments():
    queryset = Appointment.objects.all().order_by('-dateTime')
    return (queryset)

def get_measurements_by_variable(variable):
    queryset = Measurement.objects.filter(variable=variable).order_by('-dateTime')[:10]
    return (queryset)

def create_appointment(variable, measurement, limitExceeded):
    appointment = Appointment()
    appointment.variable = variable
    appointment.measurement = measurement
    appointment.value = measurement.value
    appointment.limitExceeded = limitExceeded
    appointment.save()
    return appointment