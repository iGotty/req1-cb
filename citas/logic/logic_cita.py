from measurements.models import Measurement
from ..models import Cita

def get_citas():
    queryset = Cita.objects.all().order_by('-dateTime')
    return (queryset)

def get_measurements_by_variable(variable):
    queryset = Measurement.objects.filter(variable=variable).order_by('-dateTime')[:10]
    return (queryset)

def create_cita(variable, measurement, limitExceeded):
    cita = Cita()
    cita.variable = variable
    cita.measurement = measurement
    cita.value = measurement.value
    cita.limitExceeded = limitExceeded
    cita.save()
    return cita