from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.lmsList.as_view(), name='lmsList'),
    path('create/', views.lmsCreate.as_view(), name='lmsCreate'),
    #path('<int:id>/edit/', views.lmsUpdate, name='lmsUpdate'),
    #path('<int:id>/delete/', views.lmsDelete, name='lmsDelete'),
    #path('approve/', views.lmsApprove, name='lmsApprove'),
    
]

