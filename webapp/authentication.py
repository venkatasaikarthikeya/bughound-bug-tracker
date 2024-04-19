from django.contrib.auth.backends import BaseBackend
from .models import Employee

class LoginAuthBackend(BaseBackend):

    def authenticate(self, request, loginID):
        print(loginID)
        login = Employee.objects.get(loginID=loginID)
        print(login)
        return login
