from django.contrib import admin
from django.urls import path, include

# route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('register/',include('register.urls')),
    path('home/', include('home.urls')),
    path('SmartPlug/', include('SmartPlug.urls')),
]
