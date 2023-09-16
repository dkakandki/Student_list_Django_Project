from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.signuppage, name='Signup'),
    path('login/', views.loginpage, name='login'),
    path('home/student_list/', views.home_page, name='home'),
    path('home/add_student/', views.add_student, name='Add'),
    path('home/update_student_info/<student_id>', views.update_student_info, name='update'),
    path('home/delete_student_info/<student_id>', views.delete_student, name='delete'),
    path('logout/', views.logout, name='Logout'),
]