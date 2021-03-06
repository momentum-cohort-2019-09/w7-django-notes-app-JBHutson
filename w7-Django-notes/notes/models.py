from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.updated_at = timezone.now()
        self.save()

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    note = models.ForeignKey('notes.Note', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)