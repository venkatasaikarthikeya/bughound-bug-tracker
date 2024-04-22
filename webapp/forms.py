from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, HiddenInput, Textarea
from .models import Login, Program, FunctionalArea, Employee, BugReport
from .models import levels, report_types, severities, resolutions, statuses, priorities
from django.core.exceptions import ValidationError


# Register/Create a user
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login ID', widget=TextInput(), required=True)
    password = forms.CharField(widget=HiddenInput(), required=True, help_text="Your password")
    
    class Meta:
        model = User
        fields = ['username', 'password']


# Create a Program
class CreateProgramForm(forms.ModelForm):
    
    class Meta:
        model = Program
        fields = ['name', 'version', 'release']


# Update a Program
class UpdateProgramForm(forms.ModelForm):
    
    class Meta:
        model = Program
        fields = ['name', 'version', 'release']
    

# Create a Functional Area
class CreateFunctionalAreaForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True)
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True)
    
    class Meta:
        model = FunctionalArea
        fields = ['name', 'program']


# Update a Functional Area
class UpdateFunctionalAreaForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True)
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True)
    
    class Meta:
        model = FunctionalArea
        fields = ['name', 'program']

# Filter Functional Areas
class FunctionalAreaFilterForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label="All Programs", required=False)

    class Meta:
        model = FunctionalArea
        fields = ['program']


# Create an Employee
class CreateEmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True, help_text="Employee Name")
    loginID = forms.CharField(widget=TextInput(), required=True, help_text="Employee Login ID")
    level = forms.ChoiceField(choices=levels, required=True, help_text="Employee Role")
    
    class Meta:
        model = Employee
        fields = ['name', 'loginID', 'level']


# Update an Employee
class UpdateEmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True, help_text="Employee Name")
    loginID = forms.CharField(widget=TextInput(), required=True, help_text="Employee Login ID")
    level = forms.ChoiceField(choices=levels, required=True, help_text="Employee Role")
    
    class Meta:
        model = Employee
        fields = ['name', 'loginID', 'level']


# Create a Bug Report
class CreateBugReportForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True)
    reportType = forms.ChoiceField(choices=report_types, required=True)
    severity = forms.ChoiceField(choices=severities, required=True)
    attachment = forms.CharField(widget=TextInput(), required=False)
    isReproducible = forms.BooleanField(required=True)
    problemSummary = forms.CharField(widget=TextInput(), required=True)
    problem = forms.CharField(widget=Textarea(), required=True)
    suggestedFix = forms.CharField(widget=TextInput(), required=False)
    reportedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=True)
    reportedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    # Optional Fields
    functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False)
    assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    comments = forms.CharField(widget=TextInput(), required=False)
    status = forms.ChoiceField(choices=statuses, required=False)
    priority = forms.ChoiceField(choices=priorities, required=False)
    resolution = forms.ChoiceField(choices=resolutions, required=False)
    resolvedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    resolvedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    testedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    testedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    isDeferred = forms.BooleanField(required=False)

    class Meta:
        model = BugReport
        fields = ['program', 'reportType', 'severity', 'attachment', 'problemSummary', 'isReproducible', 'problem', 'suggestedFix', 'reportedBy', 'reportedOn', 'functionalArea', 'assignedTo', 'comments', 'status', 'priority', 'resolution', 'resolvedBy', 'resolvedOn', 'testedBy', 'testedOn', 'isDeferred']


# Update a Bug Report
class UpdateBugReportForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True)
    reportType = forms.ChoiceField(choices=report_types, required=True)
    severity = forms.ChoiceField(choices=severities, required=True)
    attachment = forms.CharField(widget=TextInput(), required=False)
    isReproducible = forms.BooleanField(required=True)
    problemSummary = forms.CharField(widget=TextInput(), required=True)
    problem = forms.CharField(widget=Textarea(), required=True)
    suggestedFix = forms.CharField(widget=TextInput(), required=False)
    reportedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=True)
    reportedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    # Optional Fields
    functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False)
    assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    comments = forms.CharField(widget=TextInput(), required=False)
    status = forms.ChoiceField(choices=statuses, required=False)
    priority = forms.ChoiceField(choices=priorities, required=False)
    resolution = forms.ChoiceField(choices=resolutions, required=False)
    resolvedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    resolvedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    testedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)
    testedOn = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    isDeferred = forms.BooleanField(required=False)

    class Meta:
        model = BugReport
        fields = ['program', 'reportType', 'severity', 'attachment', 'problemSummary', 'isReproducible', 'problem', 'suggestedFix', 'reportedBy', 'reportedOn', 'functionalArea', 'assignedTo', 'comments', 'status', 'priority', 'resolution', 'resolvedBy', 'resolvedOn', 'testedBy', 'testedOn', 'isDeferred']


# Filter Bug Reports
class BugReportFilterForm(forms.Form):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label="All Programs", required=False)
    #reportType = forms.ChoiceField(choices=report_types, required=False)
    severity = forms.ChoiceField(choices=severities, required=False)
    #functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), empty_label="All Areas", required=False)
    #status = forms.ChoiceField(choices=statuses, required=False)
    #priority = forms.ChoiceField(choices=priorities, required=False)
    reportedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Any Employee", required=False)
    #assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="All Employees", required=False)
    #resolvedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="All Employees", required=False)

    class Meta:
        model = BugReport
        fields = ['program', 'severity', 'reportedBy']