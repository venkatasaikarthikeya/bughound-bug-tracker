from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateProgramForm, UpdateProgramForm, CreateEmployeeForm, UpdateEmployeeForm, CreateBugReportForm, UpdateBugReportForm
from .forms import CreateFunctionalAreaForm, UpdateFunctionalAreaForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Program, FunctionalArea, Employee, BugReport



def set_user_session(request, contextDict):
    currentUser = request.user
    currentEmployee = Employee.objects.get(loginID=currentUser.username)
    contextDict['currentUser'] = currentUser
    contextDict['currentEmployee'] = currentEmployee
    return contextDict



# Home page
def home(request):
    return render(request, 'webapp/index.html')


# Register a user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


# Login a user
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        #if form.is_valid():
        username = request.POST.get('username')
        password = 'Bugtrack@1'
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
    bugReports = BugReport.objects.all()
    context = {'bugReports': bugReports}
    context = set_user_session(request, context)
    return render(request, 'webapp/dashboard.html', context=context)


# Create Program
@login_required(login_url='login')
def create_bugreport(request):
    form = CreateBugReportForm()
    if request.method == 'POST':
        form = CreateBugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form': form}
    # context = set_user_session(request, context)
    return render(request, 'webapp/create_bugreport.html', context=context)


# Read or View a singular Bug report
@login_required(login_url='login')
def singular_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    context = {'bugReport': bugReport}
#    context = set_user_session(request, context)
    return render(request, 'webapp/view_bugreport.html', context=context)


# Update Bug report
@login_required(login_url='login')
def update_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    form = UpdateBugReportForm(instance=bugReport)
    if request.method == 'POST':
        form = UpdateBugReportForm(request.POST, instance=bugReport)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form': form}
#    context = set_user_session(request, context)
    return render(request, 'webapp/update_bugreport.html', context=context)


# Delete a Bug report
@login_required(login_url='login')
def delete_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    bugReport.delete()
    context = {}
#    context = set_user_session(request, context)
    return redirect("dashboard")

# Program List
@login_required(login_url='login')
def program_list(request):
    programs = Program.objects.all()
    context = {'programs': programs}
#    context = set_user_session(request, context)
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
#    context = set_user_session(request, context)
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
#    context = set_user_session(request, context)
    return render(request, 'webapp/update_program.html', context=context)


# Read or View a singular Program
@login_required(login_url='login')
def singular_program(request, pk):
    program = Program.objects.get(id=pk)
    context = {'program': program}
#    context = set_user_session(request, context)
    return render(request, 'webapp/view_program.html', context=context)


# Delete a Program
@login_required(login_url='login')
def delete_program(request, pk):
    program = Program.objects.get(id=pk)
    program.delete()
    context = {}
#    context = set_user_session(request, context)
    return redirect("program_list")


# Functional Area List
@login_required(login_url='login')
def functionalarea_list(request):
    functionalAreas = FunctionalArea.objects.all()
    context = {'functionalAreas': functionalAreas}
#    context = set_user_session(request, context)
    return render(request, 'webapp/functionalarea_list.html', context=context)


# Create Functional Area
@login_required(login_url='login')
def create_functionalarea(request):
    form = CreateFunctionalAreaForm()
    if request.method == 'POST':
        form = CreateFunctionalAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("functionalarea_list")
    context = {'form': form}
    context = set_user_session(request, context)
    canBeCreated = False
    if len(Program.objects.all()) > 0:
        canBeCreated = True
    else:
        context.pop('form')
    context['canBeCreated'] = canBeCreated
    return render(request, 'webapp/create_functionalarea.html', context=context)


# Update Functional Area
@login_required(login_url='login')
def update_functionalarea(request, pk):
    functionalArea = FunctionalArea.objects.get(id=pk)
    form = UpdateFunctionalAreaForm(instance=functionalArea)
    if request.method == 'POST':
        form = UpdateFunctionalAreaForm(request.POST, instance=functionalArea)
        if form.is_valid():
            form.save()
            return redirect("functionalarea_list")
    context = {'form': form}
 #   context = set_user_session(request, context)
    return render(request, 'webapp/update_functionalarea.html', context=context)


# Read or View a singular Functional Area
@login_required(login_url='login')
def singular_functionalarea(request, pk):
    functionalArea = FunctionalArea.objects.get(id=pk)
    context = {'functionalArea': functionalArea}
#    context = set_user_session(request, context)
    return render(request, 'webapp/view_functionalarea.html', context=context)


# Delete a Functional Area
@login_required(login_url='login')
def delete_functionalarea(request, pk):
    functionalArea = FunctionalArea.objects.get(id=pk)
    functionalArea.delete()
    return redirect("functionalarea_list")


# Employee List
@login_required(login_url='login')
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
#    context = set_user_session(request, context)
    return render(request, 'webapp/employee_list.html', context=context)


# Create Employee
@login_required(login_url='login')
def create_employee(request):
    form = CreateEmployeeForm()
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            User.objects.create_user(username=employee.loginID, password='Bugtrack@1')
            return redirect("employee_list")
    context = {'form': form}
#    context = set_user_session(request, context)
    return render(request, 'webapp/create_employee.html', context=context)


# Update Employee
@login_required(login_url='login')
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = UpdateEmployeeForm(instance=employee)
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    context = {'form': form}
#    context = set_user_session(request, context)
    return render(request, 'webapp/update_employee.html', context=context)


# Read or View a singular employee
@login_required(login_url='login')
def singular_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    context = {'employee': employee}
#    context = set_user_session(request, context)
    return render(request, 'webapp/view_employee.html', context=context)


# Delete Employee
@login_required(login_url='login')
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    User.objects.get(username=employee.loginID).delete()
    employee.delete()
    return redirect("employee_list")