from django.test import TestCase
from instructor.models import InstructorUser
# Testing models

class InstructorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        InstructorUser.objects.create(full_name="Peter Jackson", email="p.jackson@gmail.com")

    def test_full_name_label(self):
        instructor = InstructorUser.objects.get(id=1)
        field_label = instructor._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, "full name")

    def test_email_label(self):
        instructor = InstructorUser.objects.get(id=1)
        field_label = instructor._meta.get_field('email').verbose_name
        self.assertEqual(field_label, "email address")
    
    def test_is_admin_label(self):
        instructor = InstructorUser.objects.get(id=1)
        field_label = instructor._meta.get_field('is_admin').verbose_name
        self.assertEqual(field_label, "is admin")
    
    def test_is_active_label(self):
        instructor = InstructorUser.objects.get(id=1)
        field_label = instructor._meta.get_field('is_active').verbose_name
        self.assertEqual(field_label, "is active")
    
    def test_full_name_max_length(self):
        instructor = InstructorUser.objects.get(id=1)
        max_length = instructor._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        instructor = InstructorUser.objects.get(id=1)
        max_length = instructor._meta.get_field('email').max_length
        self.assertEqual(max_length, 255)

    def test_str(self):
        instructor = InstructorUser.objects.get(id=1)
        self.assertEqual(instructor.__str__(), instructor.full_name)