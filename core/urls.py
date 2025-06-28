from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('api/projects/', include('project.urls')),
    path('api/', include('feedback.urls')),
    path('api/project/', include('reference.urls')),
]
