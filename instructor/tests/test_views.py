from django.test import TestCase
from django.urls import reverse


from instructor.urls import *
from instructor.models import *
from student.models import Student
from game.models import Game

#Testing endpoints


class InstructorRegistrationViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    
    def setUp(self):
        test_user1 = InstructorUser.objects.create_user(email='testuser1@gmail.com', full_name="test user1", 
        password='1X<ISRUkw+tuK')
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructor/instructor-registration.html')
    
    def test_registration_post_request(self):
        test_user2_data = {'full data': "test user2", 
        'email':'testuser2@gmail.com',
        'password1':'1X<ISRUkw+tuK',
        'password2':'1X<ISRUkw+tuK'}
        response = self.client.post(reverse('register'), test_user2_data)
        #content_type ='application/x-www-form-urlencoded'
        
        #here we should be redirected to login
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'instructor/instructor-registration.html')
        #self.assertRedirects(response, reverse('login'))
        

class InstructorLoginViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    
    def setUp(self):
        test_user1 = InstructorUser.objects.create_user(email='testuser1@gmail.com', full_name="test user1", 
        password='1X<ISRUkw+tuK')
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructor/instructor-login.html')
    
    def test_login_post_request(self):
        test_user1_data = {'full data': "test user1", 
        'email':'testuser1@gmail.com',
        'password':'1X<ISRUkw+tuK'}
    
        response = self.client.post(reverse('login'), test_user1_data)        
        
        #here we should be redirected to login
        self.assertEqual(response.status_code, 200)
        #self.assertRedirects(response, reverse('dashboard'))
        


#test classes for routes which require login
class InstructorDashboardViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    def setUp(self):
        test_user1 = InstructorUser.objects.create_user(email='testuser1@gmail.com', full_name="test user1", 
        password='1X<ISRUkw+tuK')
        test_user2 = InstructorUser.objects.create_user(email='testuser2@gmail.com',full_name="test user2", 
        password='2HJ1vRV0Z&3iD')

    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/login/?next=%2Fdashboard%2F')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(email='testuser1@gmail.com', password='1X<ISRUkw+tuK')

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructor/dashboard.html')


class CreateGameViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    def setUp(self):
        test_user1 = InstructorUser.objects.create_user(email='testuser1@gmail.com', full_name="test user1", 
        password='1X<ISRUkw+tuK')
        test_user2 = InstructorUser.objects.create_user(email='testuser2@gmail.com',full_name="test user2", 
        password='2HJ1vRV0Z&3iD')

    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('create-game'))
        self.assertRedirects(response, '/login/?next=%2Fcreate-game%2F')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(email='testuser1@gmail.com', password='1X<ISRUkw+tuK')

        response = self.client.get(reverse('create-game'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructor/create-game.html')

class GamesListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    def setUp(self):
        test_user1 = InstructorUser.objects.create_user(email='testuser1@gmail.com', full_name="test user1", 
        password='1X<ISRUkw+tuK')
        test_user2 = InstructorUser.objects.create_user(email='testuser2@gmail.com',full_name="test user2", 
        password='2HJ1vRV0Z&3iD')

    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('games-list'))
        self.assertRedirects(response, '/login/?next=%2Fgames-list%2F')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(email='testuser1@gmail.com', password='1X<ISRUkw+tuK')

        response = self.client.get(reverse('games-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'instructor/games-list.html')


#feel free to make testcases for these paths
class GameUpdateViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass
    
   
class GameDeleteViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       pass

   