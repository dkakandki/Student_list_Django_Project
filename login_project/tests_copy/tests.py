from django.urls import reverse
from django.contrib.auth.models import User
from login.models import Student
from django.contrib.auth import authenticate
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def user():
    user = User.objects.create_user(username= 'Kakandki', email= '', password= 'kakandki')
    return user

@pytest.fixture
def student():
    student = Student.objects.create(
        id = 1,
        name = 'Divya Shree K',
        roll_num = 3,
        city = 'Hospet',
        marks = 98,
    )
    return student

@pytest.mark.django_db
def test_redirect_from_startPage_to_login():
    client = APIClient()
    redirect_url = reverse('login')
    response = client.get(redirect_url)
    assert response.status_code == 200

@pytest.mark.django_db   
def test_userlogin_for_correct_credentals(user):
    username = user.username
    password = 'kakandki'
    user = authenticate(username=username, password=password)
    assert user is not None
    assert user.is_authenticated
    
@pytest.mark.django_db
def test_userlogin_for_incorrect_credentals(user):
    user = authenticate(username ='incorrect', password='incorrect')
    assert user is None
   
@pytest.mark.django_db 
def test_redirect_from_login_to_home():
    client = APIClient()
    redirect_url = reverse('home')
    response = client.get(redirect_url)
    assert response.status_code == 302


@pytest.mark.studentadd
@pytest.mark.django_db
def test_student_added(student):
    client = APIClient()
    student_data = {
        'id': student.id,
        'name': student.name,
        'roll_num': student.roll_num,
        'city': student.city,
        'marks': student.marks
    }
    response = client.post(reverse('Add'), data = student_data)
    assert response.status_code == 200
    added_student = Student.objects.get(name='Divya Shree K')
    assert added_student is not None
 
@pytest.mark.studentchanges
class TestClass: 
 @pytest.mark.django_db 
 def test_student_updated(self, student):
    client = APIClient()
    student_details = {
        'id': student.id,
        'name': 'Divya Jolad',
        'roll_num': student.roll_num,
        'city': 'Gulbarga',
        'marks': student.marks
    }
    print('student data:',student)
    response = client.post(reverse('update',kwargs={'student_id': student.id}), data = student_details)
    assert response.status_code == 302
    updated_student = Student.objects.get(id=student.id)
    print('updated student:',updated_student)
    assert student.name != updated_student.name
    assert student.city != updated_student.city
    assert updated_student is not None
    
 @pytest.mark.django_db
 def test_student_deleted(self, student):
    client = APIClient()
    response = client.post(reverse('delete',kwargs={'student_id': student.id}))
    assert response.status_code == 302
    with pytest.raises(Student.DoesNotExist):
        Student.objects.get(id=student.id)
        
@pytest.mark.sanity 
def test_logout():
    client = APIClient()
    redirect_url = reverse('Logout')
    response = client.get(redirect_url)
    assert response.status_code == 302