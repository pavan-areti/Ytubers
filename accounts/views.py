from django.shortcuts import redirect,render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are succesfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'accounts/login.html')
def logoutuser(request):
    logout(request)
    return redirect('home')
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username was already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email was already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    user.save()
                    messages.success(request,"registration succesful")
                    return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('register')
        # user = User.objects.create_user(firstname=firstname,lastname=lastname,username=username,email=email,password=password)
        # user.save()
        # messages.success(request,'succesfully registered')
        # return redirect('login')

    return render(request,'accounts/register.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
