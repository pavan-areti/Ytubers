from django.urls import path,re_path
from basicapp import views

urlpatterns = [
 path('',views.home,name='home'),
 path('about',views.about,name="about"),
 path('services',views.services,name="services"),
 path('contact',views.contact,name="contact"),
]
