from django.db import models
from datetime import datetime
# Create your models here.
class hiretuber(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=200)
    user_id =  models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField()
    def __str__(self):
        return self.email
