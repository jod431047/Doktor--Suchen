from django.shortcuts import render
from django.contrib.auth.models import User



def doctors_list(request):
    doctors = User.objects.all()
    return render(request , 'user/app.html', {})