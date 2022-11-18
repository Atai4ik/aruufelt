from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
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
