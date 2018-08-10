from django.urls import path
from . import views

urlpatterns = [
    path('', views.lmsList.as_view(), name='lmsList'),
    path('approve/', views.lmsApprove.as_view(), name='lmsApprove'),
    path('create/', views.lmsCreate.as_view(), name='lmsCreate'),
    path('<int:pk>/edit/', views.lmsUpdate.as_view(), name='lmsUpdate'),
    path('<int:pk>/delete/', views.lmsDelete.as_view(), name='lmsDelete'),
    #path('approve/', views.lmsApprove, name='lmsApprove'),
    
]

