from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer



from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(req):
    return render(req, 'main.html', {'STATIC_URL': settings.STATIC_URL})