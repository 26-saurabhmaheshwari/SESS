from django.conf.urls import url
from rest_framework import routers
from django.urls import path
from api.views import StudentViewSet, UniversityViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('home/', views.home, name='profile'),
]