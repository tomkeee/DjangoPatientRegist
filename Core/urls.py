"""Core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from account.views import register_view, login_view, logout_view, home_view
from schedule.views import booking_create_view, booking_list_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view),
    path('register/',register_view),
    path('logout/',logout_view),
    path('book/',booking_create_view),
    path('ls',booking_list_view),
    path('doctor/',include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('',home_view)
]