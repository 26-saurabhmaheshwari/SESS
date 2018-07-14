"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
#from django.views.generic import AboutView
# from ems.views import AboutView, YAboutView

urlpatterns = [
    #path('', views.EmployeeListView, name='list'),
   # path('', views.index, name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('', views.EmployeeListView.as_view(), name='employee'),

    path('list/', views.EmployeeListView1, name='list'),
    path('create/', views.EmployeeCreateView, name='create'),
    path('<int:emp_no>/', views.EmployeeDetailView1, name='detail'),
    path('<int:emp_no>/edit/', views.EmployeeUpdateView, name='update'),
    path('<int:emp_no>/delete/', views.EmployeeDeleteView, name='delete'),
]