from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    buttontext = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    fbpage = models.URLField()
    instapage = models.URLField()
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)
