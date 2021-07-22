from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class youtuber(models.Model):

    crew_option = (
    ('solo','solo'),
    ('small','small-team(2-5)'),
    ('large','large-team(5+)'),
    )

    camera_option = (
    ('nicon','nicon'),
    ('panasonic','panasonic'),
    ('fuji','fuji'),
    ('red','red'),
    ('sony','sony'),
    ('canon','canon'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/')
    videourl = models.CharField(max_length=200)
    description = RichTextField()
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.IntegerField()
    camera_type=models.CharField(choices=camera_option,max_length=50)
    subs_count = models.CharField(max_length=50)
    crew = models.CharField(choices=crew_option,max_length=50)
    category = models.CharField(max_length=50)
    isfeatured = models.BooleanField(default=False)
    createddate = models.DateTimeField(default=datetime.now,blank=True)
