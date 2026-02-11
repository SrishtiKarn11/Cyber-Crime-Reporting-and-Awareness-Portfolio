from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    CRIME_CHOICES = [
        ('Fraud', 'Online Fraud'),
        ('Hacking', 'Hacking'),
        ('Harassment', 'Cyber Harassment'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crime_type = models.CharField(max_length=50, choices=CRIME_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crime_type
    
class AwarenessPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

