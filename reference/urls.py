from django.urls import path
from .views import AddReferenceView, ReferenceListView

urlpatterns = [
    path('<int:project_id>/add-reference/', AddReferenceView.as_view(), name='add-reference'),
    path('<int:project_id>/references/', ReferenceListView.as_view(), name='list-references'),
]
