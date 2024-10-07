from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', home_page),
    path('bitiruvchilar/', bitiruvchilar),
    path('students/<int:student_id>/', student_info)
]
