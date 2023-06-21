from django.shortcuts import render
from .models import Event
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegForm, LoginForm, EventForm
from django.contrib.auth.views import LoginView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    print("here")
    if request.method == 'POST':
        form = RegForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'msg': 'Registration Successful'})
        else:
            return render(request, 'home.html', {'error': form.errors.items})
    else:
        form = RegForm()
    context = {'form': form}
    print("gaga")
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        # print(form)
        if form.is_valid():
            auth_login(request, form.get_user())
            return render(request, 'home.html', {'msg': 'Login Successful'})
        else:
            print(form.errors.as_data())
            return render(request, 'home.html', {'msg': form.errors.as_data()})
    else:
        form = LoginForm()
    print("enter")
    context = {'form': form}
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def post_event(request):
    form = EventForm()
    print("post event")
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print("saved")
            prj = form.save()
            prj.user = request.user
            prj.save()
            return render(request, 'add_event.html', {'msg': 'Event added successfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'add_event.html', {'msg': 'Form invalid : '+form.errors.as_data()})
    context = {'form': form}
    return render(request, 'add_event.html', context)


def get_event(request):
    event_data = Event.objects.all().order_by('event_date', 'event_time')
    print(event_data)
    main = {'event': event_data, }
    return render(request, 'event.html', main)


def details(request, id):
    event_set = Event.objects.filter(id=id)
    context = {'event_set': event_set}
    return render(request, 'details.html', context)
