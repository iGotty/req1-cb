from django.http import JsonResponse
from django.shortcuts import render
from .models import Appointment

def schedule_appointment(request, hora, lugar):
    if 8 <= hora <= 17:
        appointment = Appointment.objects.create(hora=hora, lugar=lugar)
        return JsonResponse({'message': 'Appointment created', 'id': appointment.id})
    else:
        return JsonResponse({'message': 'Invalid hour for an appointment'}, status=400)

def appointment_list(request):
    appointments = Appointment.objects.all().values()
    return JsonResponse(list(appointments), safe=False)