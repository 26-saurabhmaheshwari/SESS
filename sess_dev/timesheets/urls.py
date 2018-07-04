from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeSheetMenu, name='timeSheetMenu'),
    path('view/', views.timeEntryList, name='timeEntryList'),
    path('create/', views.timeEntryCreate, name='timeEntryCreate'),
    path('update/', views.timeEntryUpdate, name='timeEntryUpdate'),
    path('delete/', views.timeEntryDelete, name='timeEntryDelete'),
]