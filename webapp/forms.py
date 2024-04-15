from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Program

# Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Program Manager Form
class ProgramForm(forms.ModelForm):
    programName = forms.CharField(widget=TextInput())


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
    