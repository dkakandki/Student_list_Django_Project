from django.urls import reverse
from login.models import Student
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def data():
    student1 = Student.objects.create(
        id = 1,
        name = 'Divya Shree K',
        roll_num = 3,
        city = 'Hospet',
        marks = 100,
    )
    student2 = Student.objects.create(
        id = 2,
        name = 'Anu',
        roll_num = 4,
        city = 'Hospet',
        marks = 98,
    )
    return student1,student2
     
@pytest.mark.django_db    
def test_model_str(data):
    student1, _ = data
    expected_str = 'Divya Shree K'
    assert str(student1.name) == expected_str

@pytest.mark.django_db 
def test__student_details(data):
    student1,student2 = data
    assert student1.id != student2.id
    assert len(student1.name) <= 20
    assert student1.roll_num != student2.roll_num
    assert len(student1.city) <= 20
    assert student1.marks <= 100
           