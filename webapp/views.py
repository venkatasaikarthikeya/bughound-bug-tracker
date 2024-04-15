from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateProgramForm, UpdateProgramForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Program

# Home page
def home(request):
    return render(request, 'webapp/index.html')


# Register a user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


# Login a user
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)


# User logout
def logout(request):
    auth.logout(request)
    return redirect("login")
    

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'webapp/dashboard.html')


# Program List
@login_required(login_url='login')
def program_list(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'webapp/program_list.html', context=context)


# Create Program
@login_required(login_url='login')
def create_program(request):
    form = CreateProgramForm()
    if request.method == 'POST':
        form = CreateProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("program_list")
    context = {'form': form}
    return render(request, 'webapp/create_program.html', context=context)


# Update Program
@login_required(login_url='login')
def update_program(request, pk):
    program = Program.objects.get(id=pk)
    form = UpdateProgramForm(instance=program)
    if request.method == 'POST':
        form = UpdateProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect("program_list")
    context = {'form': form}
    return render(request, 'webapp/update_program.html', context=context)


# Read or View a singular Program
@login_required(login_url='login')
def singular_program(request, pk):
    program = Program.objects.get(id=pk)
    context = {'program': program}
    return render(request, 'webapp/view_program.html', context=context)


# Delete a Program
@login_required(login_url='login')
def delete_program(request, pk):
    program = Program.objects.get(id=pk)
    program.delete()
    return redirect("program_list")