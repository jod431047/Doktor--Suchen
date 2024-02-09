from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile



def doctors_list(request):
    doctors = Profile.objects.all()
    return render(request , 'user/doctors_list.html', {
        'doctors' : doctors,
    })