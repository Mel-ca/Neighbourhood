"""neighbourhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views
from registration.backends.simple.views import RegistrationView
from neighborhood.forms import RegisterForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('neighborhood.urls')),
    path('accounts/register/$',
        RegistrationView.as_view(
            form_class=RegisterForm
        ),
        name='registration_register',
    ),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/$', views.logout, {"next_page": '/'}), 
    path('tinymce/', include('tinymce.urls')),
    
]
