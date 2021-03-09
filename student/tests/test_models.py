from django.test import TestCase
from student.models import Student
# Testing student model

class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Student.objects.create(full_name="Good Student", email="g.student@gmail.com")

    def test_full_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, "full name")

    def test_email_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('email').verbose_name
        self.assertEqual(field_label, "email")
    
    def test_time_registered_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('time_registered').verbose_name
        self.assertEqual(field_label, "time registered")
    
    def test_assigned_games_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('assigned_games').verbose_name
        self.assertEqual(field_label, "assigned games")
    
    def test_instructor_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('instructor_name').verbose_name
        self.assertEqual(field_label, "instructor name")

    def test_full_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_str(self):
        student = Student.objects.get(id=1)
        self.assertEqual(student.__str__(), student.full_name)

    # i am not testing assigned_games field except from label, because it can be changed