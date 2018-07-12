from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeSheetMenu, name='timeSheetMenu'),
    path('view/', views.timeEntryList, name='timeEntryList'),
    path('create/', views.timeEntryCreate, name='timeEntryCreate'),
    path('<int:id>/edit/', views.timeEntryUpdate, name='timeEntryUpdate'),
    path('<int:id>/delete/', views.timeEntryDelete, name='timeEntryDelete'),
    path('export/', views.timeEntryExport, name='timeEntryExport'),
    
]