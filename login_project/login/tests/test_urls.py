from django.test import SimpleTestCase
from django.urls import reverse, resolve
from login.views import  signuppage, loginpage, home_page, student_list, update_student_info, delete_student, logout

class TestUrls(SimpleTestCase):
    def test_Signup(self):
        Url = reverse('Signup')
        self.assertEqual(resolve(Url).func, signuppage)
        
    def test_Login(self):
        Url = reverse('login')
        self.assertEqual(resolve(Url).func, loginpage) 
           
    def test_Home(self):
        Url = reverse('home')
        self.assertEqual(resolve(Url).func, home_page)
        
    def test_Student_list(self):
        Url = reverse('List')
        self.assertEqual(resolve(Url).func, student_list)        

    def test_update_student(self):
        Url = reverse('update', args=['some-student_id'])
        self.assertEqual(resolve(Url).func, update_student_info) 
        
    def test_Delete(self):
        Url = reverse('delete', args=['some-student_id'])
        self.assertEqual(resolve(Url).func, delete_student) 
        
    def test_Logout(self):
        Url = reverse('Logout')
        self.assertEqual(resolve(Url).func, logout)          