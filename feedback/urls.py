from django.urls import path
from .views import UploadFeedbackView, AssignChapterToFeedbackView

urlpatterns = [
    path('api/projects/<int:project_id>/upload-feedback/', UploadFeedbackView.as_view(), name='upload-feedback'),
    path('api/feedback/<int:pk>/assign-chapter/', AssignChapterToFeedbackView.as_view(), name='assign-feedback-chapter'),
]
