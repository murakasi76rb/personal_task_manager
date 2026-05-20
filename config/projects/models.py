from django.db import models
from django.conf import settings

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'title'],
                name='unique_title_per_owner'
                                    )
        ]
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
