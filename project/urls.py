from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView


urlpatterns = [
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
]
