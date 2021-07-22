from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import youtuber
# Create your views here.
def home(request):
    slider = Slider.objects.all()
    teams = Team.objects.all()
    youtubers = youtuber.objects.order_by('-createddate').filter(isfeatured=True)
    all_tubers = youtuber.objects.all()
    data = {
    'slider' : slider,
    'teams' : teams,
    'youtubers' : youtubers,
    'all_tubers' : all_tubers,
    }
    return render(request,'basicapp/home.html',data)
def about(request):
    return render(request,'basicapp/about.html')
def services(request):
    return render(request,'basicapp/services.html')
def contact(request):
    return render(request,'basicapp/contact.html')
