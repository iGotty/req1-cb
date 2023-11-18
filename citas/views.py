from django.http import JsonResponse
from django.shortcuts import render
from .models import Cita

from .logic.logic_cita import get_citas, get_measurements_by_variable

def generate_cita(request, hora, lugar):
    if 8 <= hora <= 17:
        cita = Cita.objects.create(hora=hora, lugar=lugar)
        return JsonResponse({'message': 'Cita created', 'id': cita.id})
    else:
        return JsonResponse({'message': 'Invalid hour for a cita'}, status=400)

def cita_list(request):
    citas = get_citas()
    context = list(citas.values())
    return JsonResponse(context, safe=False)
