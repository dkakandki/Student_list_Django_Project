"""
URL configuration for login_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name='Signup'),
    path('login/', views.loginpage, name='login'),
    path('home/student_list/', views.home_page, name='home'),
    path('home/add_student/', views.add_student, name='Add'),
    path('home/update_student_info/<student_id>', views.update_student_info, name='update'),
    path('home/delete_student_info/<student_id>', views.delete_student, name='delete'),
    path('logout/', views.logout, name='Logout'),
    path('login/', include('login.urls')),
]


