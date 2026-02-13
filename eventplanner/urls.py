"""
URL configuration for eventplanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

# The main URL patterns for the project
# This file acts as the "root router" that directs requests to the correct app
urlpatterns = [
    # Route for Django’s built-in admin interface
    # Visiting http://127.0.0.1:8000/admin/ will open the admin login page
    path('admin/', admin.site.urls),

    # Route for the API endpoints defined in the "api" app
    # Visiting http://127.0.0.1:8000/api/ will load the URL patterns from api/urls.py
    # This keeps the project modular: all API routes are managed inside the api app
    path('api/', include('api.urls')),
]
