from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creatd_date'] #newset review first
        unique_together = ['movie_title','user'] #one review per movie per user

    def __str__(self):
        return f"{self.user.username} - {self.movie_title} ({self.rating}/5)"