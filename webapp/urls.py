from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name = ""),
      path('register', views.register, name = "register"),
      path('login', views.login, name = "login"),
      path('logout', views.logout, name = "logout"),

      # CRUD operations on BugReport
      path('dashboard', views.dashboard, name = "dashboard"),
      path('bugreport/<int:pk>', views.singular_bugreport, name = "bugreport"),
      path('create_bugreport', views.create_bugreport, name = "create_bugreport"),
      path('update_bugreport/<int:pk>', views.update_bugreport, name = "update_bugreport"),
      path('view_attachment/<int:pk>', views.view_attachment, name = "view_attachment"),
      path('delete_bugreport/<int:pk>', views.delete_bugreport, name = "delete_bugreport"),

      # CRUD operations on Program
      path('program_list', views.program_list, name = "program_list"),
      path('program/<int:pk>', views.singular_program, name = "program"),
      path('create_program', views.create_program, name = "create_program"),
      path('update_program/<int:pk>', views.update_program, name = "update_program"),
      path('delete_program/<int:pk>', views.delete_program, name = "delete_program"),

      # CRUD operations on Functional Area
      path('functionalarea_list', views.functionalarea_list, name = "functionalarea_list"),
      path('create_functionalarea', views.create_functionalarea, name = "create_functionalarea"),
      path('functionalarea/<int:pk>', views.singular_functionalarea, name = "functionalarea"),
      path('update_functionalarea/<int:pk>', views.update_functionalarea, name = "update_functionalarea"),
      path('delete_functionalarea/<int:pk>', views.delete_functionalarea, name = "delete_functionalarea"),
      path('export_area', views.export_area, name='export_area'),

      # CRUD operations on Employee
      path('employee_list', views.employee_list, name = "employee_list"),
      path('create_employee', views.create_employee, name = "create_employee"),
      path('employee/<int:pk>', views.singular_employee, name = "employee"),
      path('update_employee/<int:pk>', views.update_employee, name = "update_employee"),
      path('delete_employee/<int:pk>', views.delete_employee, name = "delete_employee"),
      path('export_employee', views.export_employee, name='export_employee'),
]