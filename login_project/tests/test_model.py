from django.test import TestCase, Client
from login.models import Student

class TestModels(TestCase):
    def setUp(self):
        self.student1 = Student.objects.create(
            id = 1,
            name = 'Divya Shree K',
            roll_num = 3,
            city = 'Hospet',
            marks = 100,
        )
        self.student2 = Student.objects.create(
            id = 2,
            name = 'Anu',
            roll_num = 4,
            city = 'Hospet',
            marks = 98,
        )
        
    def test_model_str(self):
        self.assertEqual(str(self.student1.name), 'Divya Shree K')
        
    def test__student_details(self):
        self.assertNotEqual(self.student1.id, self.student2.id)
        self.assertLessEqual(len(self.student1.name),20)
        self.assertNotEqual(self.student1.roll_num, self.student2.roll_num)
        self.assertLessEqual(len(self.student1.city),20)
        self.assertLessEqual(self.student1.marks,100)
           