from django.http import JsonResponse
from django.shortcuts import render

from variables.logic.variable_logic import get_variable_by_id
from .logic.logic_cita import get_citas, get_measurements_by_variable, create_cita

def cita_list(request):
    citas = get_citas()
    context = list(citas.values())
    return JsonResponse(context, safe=False)

def generate_cita(request, variable_id):
    variable = get_variable_by_id(variable_id)
    measurements = get_measurements_by_variable(variable_id)
    createCita = False
    upperMeasurement = None
    for measurement in measurements:
        if measurement.value >= 30:
            createCita = True
            upperMeasurement = measurement
    if createCita:
        cita = create_cita(variable, upperMeasurement, 30)
        return JsonResponse(cita.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No cita created'}, status=200)