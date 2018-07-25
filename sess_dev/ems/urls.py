from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),           # To make login work correctly 
    path('<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('', views.EmployeeListView.as_view(), name='employee'),
    path('create/', views.EmployeeCreateView, name='create'),
    path('<int:id>/edit/', views.EmployeeUpdateView, name='update'),
    path('<int:id>/delete/', views.EmployeeDeleteView, name='delete'),
]