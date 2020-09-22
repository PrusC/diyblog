from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
# Create your models here.


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        verbose_name="user's avatar", 
        name='avatar', 
        null=True,
        blank=True)


    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('profile-detail', args=[str(self.id)])


    @property
    def first_name(self):
        self.user.first_name

    @property
    def last_name(self):
        self.user.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)

    # def get_absolute_url(self):
    #     return reverse('post-detail', args=[str(self.id)])