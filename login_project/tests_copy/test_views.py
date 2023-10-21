from django.urls import reverse
from login.models import Student
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def student():
    return Student.objects.create(
        id = 1,
        name = 'Divya Shree K',
        roll_num = 3,
        city = 'Hospet',
        marks = 98,
    )
        
# def test_home_page_GET():
#     client = APIClient()
#     response = client.get(reverse('home'))
#     assert response.status_code == 302
#     # assert '/login/?next=/home/student_list/' in [template.name for template in response]
        
def test_Add_Student_POST():
    client = APIClient()
    response = client.post(reverse('Add'))
    assert response.status_code == 200
    assert 'registration/add_student.html' in [template.name for template in response.templates]
    
@pytest.mark.django_db
def test_update_Student_POST(student):
    client = APIClient()
    url = reverse('update', kwargs={'student_id': student.id})
    response = client.post(url)
    assert 'registration/update_student_info.html' in [template.name for template in response.templates]
        
@pytest.mark.django_db        
def test_delete_Student_POST(student):
    client = APIClient()
    url = reverse('delete', kwargs={'student_id': student.id})
    response = client.delete(url)
    assert response.status_code == 302
          