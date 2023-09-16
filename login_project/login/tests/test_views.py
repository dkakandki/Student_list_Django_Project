from django.test import TestCase, Client
from django.urls import reverse
from login.models import Student

class TestViews(TestCase):
    def test_Student_List_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/home.html')
        
    def test_Add_Student_POST(self):
        client = Client()
        response = client.post(reverse('List'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/Student_list.html')  
        
    def test_login(self):
        client = Client()
        response = client.post(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')   
        
    def test_signup(self):
        client = Client()
        response = client.post(reverse('Signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        
    def test_Update_Student_info(self):
        client = Client(arg = ['some-student_id'])
        response = client.put(reverse('update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/update_student_info.html')
    
    def test_Update_Student_info(self):
        client = Client(arg = ['some-student_id'])
        response = client.delete(reverse('delete'))
        self.assertEqual(response.status_code, 200)
              