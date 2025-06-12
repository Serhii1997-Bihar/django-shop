from django.db import models
from django.contrib.auth.models import User
import os

class PathMedia:
    @staticmethod
    def user_avatar(instance, filename):
        return os.path.join('users_images', instance.user.username, filename)

    @staticmethod
    def user_images(instance, filename):
        return os.path.join('users_images', instance.gallery.user.username, 'images', filename)

    @staticmethod
    def user_videos(instance, filename):
        return os.path.join('users_images', instance.gallery.user.username, 'videos', filename)

class GalleryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Основний User', blank=True)
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереї'

    def __str__(self):
        return self.user.username if self.user else "No user"

class ImagesUser(models.Model):
    gallery = models.ForeignKey(GalleryUser, on_delete=models.CASCADE, verbose_name='Основний User', blank=True)
    images = models.ImageField(upload_to=PathMedia.user_images, verbose_name='Зображення', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

class VideosUser(models.Model):
    gallery = models.ForeignKey(GalleryUser, on_delete=models.CASCADE, verbose_name='Основний User', blank=True)
    videos = models.FileField(upload_to=PathMedia.user_videos, verbose_name='Відео', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

class MessageUser(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.content[:20]}..."

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Основний User', blank=True, null=True)
    birth = models.DateField(blank=True, verbose_name='Народження', null=True)
    photo = models.ImageField(upload_to=PathMedia.user_avatar, verbose_name='Основна світлина', blank=True)
    hobby = models.CharField(max_length=400, blank=True, verbose_name='Хоббі')
    city = models.CharField(max_length=40, blank=True, verbose_name='Місто')
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True)
    info = models.TextField(blank=True, verbose_name='Інформація')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.user.username if self.user else "No user"


