from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name = ""),
      path('register', views.register, name = "register"),
      path('login', views.login, name = "login"),
      path('logout', views.logout, name = "logout"),
      path('dashboard', views.dashboard, name = "dashboard"),

      # CRUD operations on Program
      path('program_list', views.program_list, name = "program_list"),
      path('program/<int:pk>', views.singular_program, name = "program"),
      path('create_program', views.create_program, name = "create_program"),
      path('update_program/<int:pk>', views.update_program, name = "update_program"),
      path('delete_program/<int:pk>', views.delete_program, name = "delete_program"),

      # CRUD operations on Functional Area
      path('functionalarea_list', views.functionalarea_list, name = "functionalarea_list"),
      path('functionalarea/<int:pk>', views.singular_functionalarea, name = "functionalarea"),
      path('create_functionalarea', views.create_functionalarea, name = "create_functionalarea"),
      path('update_functionalarea/<int:pk>', views.update_functionalarea, name = "update_functionalarea"),
      path('delete_functionalarea/<int:pk>', views.delete_functionalarea, name = "delete_functionalarea"),
]