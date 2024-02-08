from django.urls import path 

from . import views
app_name = 'todo'

urlpatterns = [
    path('app/' ,views.app , name='app'),
]
