from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Program, FunctionalArea, Employee, roles


# Register/Create a user
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=TextInput(), required=True, help_text="Your username")
    first_name = forms.CharField(widget=TextInput(), required=True, help_text="Your first name")
    last_name = forms.CharField(widget=TextInput(), required=True, help_text="Your last name")
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', ]


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(), required=True, help_text="Your username")
    password = forms.CharField(widget=PasswordInput(), required=True, help_text="Your password")
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
    class Meta:
        model = FunctionalArea
        fields = ['name', 'description']


# Update a Functional Area
class UpdateFunctionalAreaForm(forms.ModelForm):
    class Meta:
        model = FunctionalArea
        fields = ['name', 'description']


# Create an Employee
class CreateEmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True, help_text="Employee Name")
    email = forms.CharField(widget=TextInput(), required=True, help_text="Employee Email")
    role = forms.ChoiceField(choices=roles, required=True, help_text="Employee Role")
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, help_text="Employee User")
    class Meta:
        model = Employee
        fields = ['name', 'email', 'role', 'user']


# Update an Employee
class UpdateEmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(), required=True, help_text="Employee Name")
    email = forms.CharField(widget=TextInput(), required=True, help_text="Employee Email")
    role = forms.ChoiceField(choices=roles, required=True, help_text="Employee Role")
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, help_text="Employee User")
    class Meta:
        model = Employee
        fields = ['name', 'email', 'role', 'user']