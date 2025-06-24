from django.db import models
from project.models import Project

class Reference(models.Model):
    STYLE_CHOICES = [
        ('APA', 'APA'),
        ('Harvard', 'Harvard'),
        ('IEEE', 'IEEE'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='references')
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, default='APA')
    citation_text = models.TextField()
    source_url = models.URLField(blank=True, null=True)
    added_manually = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.style} - {self.citation_text[:50]}"
