from django.urls import path
from . import views

urlpatterns = [
    path('', views.InboxList.as_view(), name='InboxList'),
    path('<int:pk>', views.InboxDetail.as_view(), name='InboxDetail'),

]

