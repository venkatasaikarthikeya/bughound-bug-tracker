from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateProgramForm, UpdateProgramForm, CreateEmployeeForm, UpdateEmployeeForm, CreateBugReportForm, UpdateBugReportForm, FunctionalAreaFilterForm, BugReportFilterForm
from .forms import CreateFunctionalAreaForm, UpdateFunctionalAreaForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Program, FunctionalArea, Employee, BugReport
from django.core import serializers
from django.http import HttpResponse, Http404
from django.utils import timezone
from django import forms
import os


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
    form = BugReportFilterForm(request.GET)
    bugReports = BugReport.objects.all()

    if form.is_valid():
        
        # Filter by program
        program = form.cleaned_data.get('program')
        if program:
            bugReports = bugReports.filter(program=program)

        # Filter by severity
        severity = form.cleaned_data.get('severity')
        if severity and severity != 'Select':
            bugReports = bugReports.filter(severity=severity)

        # Filter by reported by
        reportedBy = form.cleaned_data.get('reportedBy')
        if reportedBy and reportedBy != 'Any Employee':
            bugReports = bugReports.filter(reportedBy=reportedBy)

        
        # Filter by assigned to
        assignedTo = form.cleaned_data.get('assignedTo')
        if assignedTo and assignedTo != 'Any Employee':
            bugReports = bugReports.filter(assignedTo=assignedTo)

        # Filter by status
        status = form.cleaned_data.get('status')
        if status and status != 'Select':
            bugReports = bugReports.filter(status=status)
        else:
            l = []
            for bugReport in bugReports:
                if bugReport.status != 'Closed':
                    l.append(bugReport)
            bugReports = l


        '''
        # Filter by report type
        reportType = form.cleaned_data.get('reportType')
        if reportType:
            bugReports = bugReports.filter(reportType=reportType)

        

        # Filter by functional area
        functionalArea = form.cleaned_data.get('functionalArea')
        if functionalArea:
            bugReports = bugReports.filter(functionalArea=functionalArea)
        
        # Filter by priority
        priority = form.cleaned_data.get('priority')
        if priority:
            bugReports = bugReports.filter(priority=priority)

        # Filter by resolved by
        resolvedBy = form.cleaned_data.get('resolvedBy')
        if resolvedBy:
            bugReports = bugReports.filter(resolvedBy=resolvedBy)
        '''

    context = {'bugReports': bugReports, 'form': form}
    context = set_user_session(request, context)
    return render(request, 'webapp/dashboard.html', context=context)


def control_form_visibility(form, request):
    currentUser = request.user
    currentEmployee = Employee.objects.get(loginID=currentUser.username)
    if currentEmployee.level == '1':
        form.fields['functionalArea'].widget = forms.HiddenInput()
        form.fields['assignedTo'].widget = forms.HiddenInput()
        form.fields['comments'].widget = forms.HiddenInput()
        form.fields['status'].widget = forms.HiddenInput()
        form.fields['priority'].widget = forms.HiddenInput()
        form.fields['resolution'].widget = forms.HiddenInput()
        form.fields['resolvedBy'].widget = forms.HiddenInput()
        form.fields['resolvedOn'].widget = forms.HiddenInput()
        form.fields['testedBy'].widget = forms.HiddenInput()
        form.fields['testedOn'].widget = forms.HiddenInput()
        form.fields['isDeferred'].widget = forms.HiddenInput()
    # Un hide this field when attachment is implemented
    # form.fields['attachment'].widget = forms.HiddenInput()
    return form


# Create Program
@login_required(login_url='login')
def create_bugreport(request):
    form = CreateBugReportForm()
    if request.method == 'POST':
        print(request.FILES)
        form = CreateBugReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    form = control_form_visibility(form, request)
    context = {'form': form}
    context = set_user_session(request, context)
    return render(request, 'webapp/create_bugreport.html', context=context)


# Read or View a singular Bug report
@login_required(login_url='login')
def singular_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    context = {'bugReport': bugReport}
    context = set_user_session(request, context)
    return render(request, 'webapp/view_bugreport.html', context=context)


# Update Bug report
@login_required(login_url='login')
def update_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    form = UpdateBugReportForm(instance=bugReport)
    if request.method == 'POST':
        print(request.FILES)
        form = UpdateBugReportForm(request.POST, request.FILES, instance=bugReport)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    form = control_form_visibility(form, request)
    context = {'form': form}
    context = set_user_session(request, context)
    return render(request, 'webapp/update_bugreport.html', context=context)


# View Attachment
@login_required(login_url='login')
def view_attachment(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    file_path = bugReport.attachment.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
    else:
        raise Http404("The requested file does not exist.")


# Delete a Bug report
@login_required(login_url='login')
def delete_bugreport(request, pk):
    bugReport = BugReport.objects.get(id=pk)
    if bugReport.attachment:
        file_path = bugReport.attachment.path
        if os.path.isfile(file_path):
            os.remove(file_path)
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

'''
# Functional Area List
@login_required(login_url='login')
def functionalarea_list(request):
    functionalAreas = FunctionalArea.objects.all()
    context = {'functionalAreas': functionalAreas}
#    context = set_user_session(request, context)
    return render(request, 'webapp/functionalarea_list.html', context=context)
'''

@login_required(login_url='login')
def functionalarea_list(request):
    form = FunctionalAreaFilterForm(request.GET)
    functionalAreas = FunctionalArea.objects.all()

    if form.is_valid():
        program = form.cleaned_data.get('program')
        if program:
            functionalAreas = functionalAreas.filter(program=program)

    context = {'functionalAreas': functionalAreas, 'form': form}
    return render(request, 'webapp/functionalarea_list.html', context=context)


# Export Area
@login_required(login_url='login')
def export_area(request):
    timestamp = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
    data = serializers.serialize("xml", FunctionalArea.objects.all())
    data_with_timestamp = f'{data}<!-- Timestamp: {timestamp} -->\n'
    response = HttpResponse(data_with_timestamp, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="areas.xml"'
    return response


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


# Export Employee
def export_employee(request):
    employees = Employee.objects.all()
    timestamp = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
    L = []
    L.append(f'<!-- Timestamp: {timestamp} -->\n')
    for employee in employees:
        s = str(employee.id) + ' ' + str(employee.name) + ' ' + str(employee.loginID) + ' ' + str(employee.level) + "\n"
        for character in s:
            L.append(str(ord(character)))
    response = HttpResponse(''.join(L), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="employees.txt"'
    # return render(request, 'bugtracker/export_employee.html')
    # return response
    # form = Employee.get_form()
    # data = serializers.serialize("txt", Employee.objects.all())
    # response = HttpResponse(data, content_type='text/txt')
    # response['Content-Disposition'] = 'attachment; filename="areas.txt"'
    return response