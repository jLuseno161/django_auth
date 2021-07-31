"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    # url('login/',auth_views.LoginView.as_view(), name='login'),
    # url('profile/', views.profile, name='profile'),
    # path('landingpage/',views.landingpage,name = 'landingpage'),
    url('employee_register/',views.employee_register.as_view(),name = 'employee_register'),
    url('employer_register/',views.employer_register.as_view(),name = 'employer_register'),
    url('login/',views.login_request,name = 'login'),
    url('logout/',views.logout_request,name = 'logout'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)