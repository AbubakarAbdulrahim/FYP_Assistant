from django.db import models
from project.models import Project, Chapter

# feedback upload model
class FeedbackUpload(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="feedback_uploads")
    file = models.FileField(upload_to='feedback/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

# feedback item model
class FeedbackItem(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="feedbacks", null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    comment_text = models.TextField()
    position = models.CharField(max_length=100, blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
