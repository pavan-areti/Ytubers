from django.shortcuts import render
from .models import hiretuber
# firstname = models.CharField(max_length=200)
# lastname = models.CharField(max_length=200)
# tuber_id = models.IntegerField()
# tuber_name = models.CharField(max_length=200)
# city = models.CharField(max_length=200)
# state = models.CharField(max_length=200)
# message = models.TextField()
# phone = models.CharField(max_length=200)
# user_id =  models.IntegerField()
# created_date = models.DateTimeField(default=datetime.now)
# email = models.EmailField()
# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        tuber_id = request.POST['firstname']
        tuber_name = request.POST['firstname']
        city = request.POST['firstname']
        state = request.POST['firstname']
        message = request.POST['firstname']
        phone = request.POST['firstname']
        user_id = request.POST['firstname']
        email = request.POST['email']
        tuber =  hiretuber(firstname=firstname,lastname=lastname,tuber_id=tuber_id,tuber_name=tuber_name,city=city,state=state,message=message,phone=phone,user_id=user_id,email=email)
        tuber.save()
