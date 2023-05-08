from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_delete=True)

    def query_with_kw(self, keyword):
        return self.filter(title__contains=keyword)


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=666)
    author = models.ForeignKey(User)
    # my_objects = MyManager()
    is_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return self.title


