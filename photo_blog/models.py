import os
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


def get_image_path(instance, filename):
    return os.path.join('posts', str(instance.author), filename)


class Post(models.Model):
    photo = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    caption = models.TextField(max_length=2200, null=True, blank=True)
    # hashtags = models....
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('photo_blog-detail', kwargs={'pk': self.pk})

    def get_api_like_url(self):
        return reverse('photo_blog-post_like_api', kwargs={"pk": self.pk})

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        output_size = (450, (img.height / img.width) * 450,)
        img.thumbnail(output_size)
        img.save(self.photo.path)



class Comment(models.Model):
    post = models.ForeignKey('photo_blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def save(self):
        super().save()

    def get_absolute_url(self):
        return reverse('photo_blog-comment', kwargs={'pk': self.pk})