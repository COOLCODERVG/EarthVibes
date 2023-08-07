from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .forms import EventForm
from .models import EventModel

# Create your views here.
class Home(View):
    def get(self, request):
        username = ""
        aut=request.user.is_authenticated
        print(aut)
        if request.user.is_authenticated:
            username = request.user.username
            
            print(username)
        context={"uname":username,"aut":aut}
        print( username)
        return render(request, 'base.html', context)
    

    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/')
                
        else:
            print("None")
    
def Signup(request, *args, **kwargs):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        my_user = User.objects.create_user(uname, email, passw)
        my_user.save()
        redirect('/')
    return render(request, 'signup.html')

def Login(request, *args, **kwargs):
    return render(request, 'login.html')

def Event(request, *args, **kwargs):
    print(request.method)
    aut=request.user.is_authenticated
    username=request.user.username
    context={"uname":username,"aut":aut}
    if request.method == 'POST':
        print(request.method)
        ename = request.POST.get('ename')
        edesc = request.POST.get('edesc')  
        zip = request.POST.get('zip')
        city = request.POST.get('city')  
        add = request.POST.get('add')
        date = request.POST.get('date')
        print(ename)
        m = EventModel(name = ename, author= request.user.username, date = date, zipcode = zip, city = city, address = add, description = edesc)
        m.save()
        print(m)
        return redirect('/events/')
    if request.method == 'GET':
        
        entries = EventModel.objects.all()
    return render(request, 'allevents.html', {'entries':entries,'aut':aut,'uname':username})

def logout_view(request):
    logout(request)
    return redirect('/')

def NewEvent(request):
    aut=request.user.is_authenticated
    username=request.user.username
    context={"uname":username,"aut":aut}
    return render(request, 'event.html',context)

def OurTeam(request):
    aut=request.user.is_authenticated
    username=request.user.username
    context={"uname":username,"aut":aut}
    return render(request, 'team.html',context)