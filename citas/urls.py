from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('citas/', views.cita_list),
    path('citasValidate/<int:hora>/<str:lugar>/', views.generate_cita),
]
