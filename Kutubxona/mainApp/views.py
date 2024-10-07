from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone
from .models import *


def home(request):
    return HttpResponse("<h1>Home Page</h1>")


def home_page(request):
    data = {
        'now_time': timezone.now(),
        'students': Talaba.objects.all()
    }
    return render(request, 'home.html', data)


def bitiruvchilar(request):
    context = {
        'students': Talaba.objects.filter(kurs=4)
    }
    return render(request, 'bitiruvchilar.html', context)


def student_info(request, student_id):
    # student = Talaba.objects.get(id=student_id)
    student = get_object_or_404(Talaba, id=student_id)
    context = {
        'student': student
    }
    return render(request, 'student_info.html', context)