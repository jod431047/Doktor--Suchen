from django.urls import path 

from . import views
app_name = 'todo'

urlpatterns = [
    path('doctors/' ,views.doctors_list, name='doctors_list'),
]
