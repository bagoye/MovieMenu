from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class TogetherArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles_together')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_together")

    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    

class TogetherComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_together')
    article = models.ForeignKey(TogetherArticle, on_delete=models.CASCADE, related_name='comments_together')
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FreeArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles_free')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_free")

    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
  

class FreeComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_free')
    article = models.ForeignKey(FreeArticle, on_delete=models.CASCADE, related_name='comments_free')
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
