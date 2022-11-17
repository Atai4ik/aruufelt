from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)
