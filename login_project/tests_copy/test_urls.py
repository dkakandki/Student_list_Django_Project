
from django.urls import reverse, resolve
from login.views import  signuppage, loginpage, home_page, add_student, update_student_info, delete_student, logout
import pytest

class TestUrls:
    def test_Signup(self):
        Url = reverse('Signup')
        assert resolve(Url).func == signuppage
        
    def test_Login(self):
        Url = reverse('login')
        assert resolve(Url).func == loginpage 
           
    def test_Home(self):
        Url = reverse('home')
        assert resolve(Url).func == home_page
        
    def test_add_student(self):
        Url = reverse('Add')
        assert resolve(Url).func == add_student     

    def test_update_student(self):
        Url = reverse('update', args=['some-student_id'])
        assert resolve(Url).func == update_student_info
        
    def test_Delete(self):
        Url = reverse('delete', args=['some-student_id'])
        assert resolve(Url).func == delete_student 
        
    def test_Logout(self):
        Url = reverse('Logout')
        assert resolve(Url).func == logout       