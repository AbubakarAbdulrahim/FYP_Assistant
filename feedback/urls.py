from django.urls import path
from .views import UploadFeedbackView, AssignChapterToFeedbackView

urlpatterns = [
    path('project/<int:project_id>/upload-feedback/', UploadFeedbackView.as_view(), name='upload-feedback'),
    path('feedback/<int:pk>/assign-chapter/', AssignChapterToFeedbackView.as_view(), name='assign-feedback-chapter'),
]
