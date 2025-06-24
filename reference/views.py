from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Reference
from .serializers import ReferenceSerializer


# create reference view
class AddReferenceView(generics.CreateAPIView):
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_id")
        serializer.save(project_id=project_id, added_manually=True)

# list reference view
class ReferenceListView(generics.ListAPIView):
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        return Reference.objects.filter(project_id=project_id).order_by("-created_at")
