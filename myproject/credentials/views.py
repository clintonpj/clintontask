from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'csk.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    if request.method == 'GET' and 'register' in request.GET:
        return redirect('register')

    return render(request, "login.html")





def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email Taken")
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')

        message = "Order Confirmed"

        return render(request,'confirmation.html',{'message':message})
    return render(request,'form.html')
