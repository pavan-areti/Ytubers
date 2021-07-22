from django.shortcuts import render,get_object_or_404
from .models import youtuber
# Create your views here.
def youtubers(request):
    tubers = youtuber.objects.order_by('-createddate')
    data={
    'tubers':tubers,
    }
    return render(request,'youtubers/youtubers.html',data)
def youtubers_detail(request,id):
    tuber = get_object_or_404(youtuber,pk=id)
    data={
    'tuber':tuber,
    }
    return render(request,'youtubers/youtubers_detail.html',data)
def search(request):
    tubers =  youtuber.objects.order_by('-createddate')
    cities = youtuber.objects.values_list('city',flat=True)
    camera_types = youtuber.objects.values_list('camera_type',flat=True).distinct()
    categories = youtuber.objects.values_list('category',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tubers = tubers.filter(camera_type__iexact=camera)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    data = {
    'tubers':tubers,
    'cities':cities,
    'camera_types':camera_types,
    'categories' : categories,
    }
    return render(request,'youtubers/search.html',data)
