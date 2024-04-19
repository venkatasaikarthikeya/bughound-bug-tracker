from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, HiddenInput
from .models import Login, Program, FunctionalArea, Employee, BugReport
from .models import levels, report_types, severities, resolutions, statuses, priorities


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
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True, help_text="Program")
    reportType = forms.ChoiceField(choices=report_types, required=True, help_text="Report Type")
    severity = forms.ChoiceField(choices=severities, required=True, help_text="Severity")
    attachment = forms.CharField(widget=TextInput(), required=False, help_text="Attachment")
    problemSummary = forms.CharField(widget=TextInput(), required=True, help_text="Problem Summary")
    isReproducible = forms.BooleanField(required=True, help_text="Is Reproducible")
    problem = forms.CharField(widget=TextInput(), required=False, help_text="Problem")
    suggestedFix = forms.CharField(widget=TextInput(), required=False, help_text="Suggested Fix")
    reportedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=True, help_text="Reported By")
    reportedOn = forms.DateTimeField(required=True, help_text="Reported On")
    functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False, help_text="Functional Area")
    assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Assigned To")
    comments = forms.CharField(widget=TextInput(), required=False, help_text="Comments")
    status = forms.ChoiceField(choices=statuses, required=False, help_text="Status")
    priority = forms.ChoiceField(choices=priorities, required=False, help_text="Priority")
    resolution = forms.ChoiceField(choices=resolutions, required=False, help_text="Resolution")
    resolvedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Resolved By")
    resolvedOn = forms.DateTimeField(required=False, help_text="Resolved On")
    testedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Tested By")
    testedOn = forms.DateTimeField(required=False, help_text="Tested On")
    isDeferred = forms.BooleanField(required=False, help_text="Is Deferred")

    class Meta:
        model = BugReport
        fields = ['program', 'reportType', 'severity', 'attachment', 'problemSummary', 'isReproducible', 'problem', 'suggestedFix', 'reportedBy', 'reportedOn', 'functionalArea', 'assignedTo', 'comments', 'status', 'priority', 'resolution', 'resolvedBy', 'resolvedOn', 'testedBy', 'testedOn', 'isDeferred']


# Update a Bug Report
class UpdateBugReportForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), required=True, help_text="Program")
    reportType = forms.ChoiceField(choices=report_types, required=True, help_text="Report Type")
    severity = forms.ChoiceField(choices=severities, required=True, help_text="Severity")
    attachment = forms.CharField(widget=TextInput(), required=False, help_text="Attachment")
    problemSummary = forms.CharField(widget=TextInput(), required=True, help_text="Problem Summary")
    isReproducible = forms.BooleanField(required=True, help_text="Is Reproducible")
    problem = forms.CharField(widget=TextInput(), required=False, help_text="Problem")
    suggestedFix = forms.CharField(widget=TextInput(), required=False, help_text="Suggested Fix")
    reportedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=True, help_text="Reported By")
    reportedOn = forms.DateTimeField(required=True, help_text="Reported On")
    functionalArea = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), required=False, help_text="Functional Area")
    assignedTo = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Assigned To")
    comments = forms.CharField(widget=TextInput(), required=False, help_text="Comments")
    status = forms.ChoiceField(choices=statuses, required=False, help_text="Status")
    priority = forms.ChoiceField(choices=priorities, required=False, help_text="Priority")
    resolution = forms.ChoiceField(choices=resolutions, required=False, help_text="Resolution")
    resolvedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Resolved By")
    resolvedOn = forms.DateTimeField(required=False, help_text="Resolved On")
    testedBy = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Tested By")
    testedOn = forms.DateTimeField(required=False, help_text="Tested On")
    isDeferred = forms.BooleanField(required=False, help_text="Is Deferred")

    class Meta:
        model = BugReport
        fields = ['program', 'reportType', 'severity', 'attachment', 'problemSummary', 'isReproducible', 'problem', 'suggestedFix', 'reportedBy', 'reportedOn', 'functionalArea', 'assignedTo', 'comments', 'status', 'priority', 'resolution', 'resolvedBy', 'resolvedOn', 'testedBy', 'testedOn', 'isDeferred']