from django.db import models
from user.models import User

# project model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=100)
    abstract = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('draft', 'Draft'), ('completed', 'Completed')],
        default='draft'
    )

    def __str__(self):
        return self.title
    
# chapter model
class Chapter(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="chapters")
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    generated = models.BooleanField(default=False)

    class Meta:
        unique_together = ('project', 'number')
