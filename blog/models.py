from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


    @property
    def first_name(self):
        self.user.first_name

    @property
    def last_name(self):
        self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Blogger.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.blogger.save()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=False)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=False, blank=False)
    publish = models.DateTimeField(default=timezone.now)
    