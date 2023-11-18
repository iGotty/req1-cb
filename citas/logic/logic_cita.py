from measurements.models import Measurement
from ..models import Cita

def get_citas():
    queryset = Cita.objects.all().order_by('-dateTime')
    return (queryset)

def get_measurements_by_variable(variable):
    queryset = Measurement.objects.filter(variable=variable).order_by('-dateTime')[:10]
    return (queryset)

def create_cita(hora, lugar):
    cita = Cita()
    cita.hora = hora
    cita.lugar = lugar
    cita.save()
    return cita