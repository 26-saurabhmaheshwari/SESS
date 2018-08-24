from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timesheets/', include('timesheets.urls')),
    path('lms/', include('lms.urls')),
    path('employee/', include('ems.urls'), name="em"),
    path('', views.Dashboard, name='home'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logged_out.html'},  name='logout'),
    path('error/', views.error, name='error'),

    # path('api/', include('api.urls'), name='api'),  
    # path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)