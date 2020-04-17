from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=140)
    note = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.title} {self.note} {self.completed} {self.created} {self.updated_at}'