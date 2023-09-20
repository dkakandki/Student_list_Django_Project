from django.test import TestCase, Client
from django.urls import reverse
from login.models import Student

class TestViews(TestCase):
    def test_home_page_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertTemplateUsed(response, 'registration/home.html')
        
    def test_Add_Student_POST(self):
        client = Client()
        response = client.post(reverse('Add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/add_student.html')  

    def test_update_Student_POST(self):
        client = Client()
        student = Student.objects.create(
            id = 1,
            name = 'Divya Shree K',
            roll_num = 3,
            city = 'Hospet',
            marks = 98,
        )
        url = url = reverse('update', kwargs={'student_id': student.id})
        response = client.post(url)
        self.assertTemplateUsed(response, 'registration/update_student_info.html')