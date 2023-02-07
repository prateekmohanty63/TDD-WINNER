from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from .forms import NotesForm
from django.urls import reverse

# Create your tests here.
# TDD

User=get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        user_a=User(username='testAdmin',email='testAdmin@gmail.com')

        user_a_pw="testAdminPassword"
        self.user_a_pw=user_a_pw
        user_a.is_staff=True
        user_a.is_superuser=True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a=user_a

    def test_user_exists(self):
        user_count=User.objects.all().count()
        self.assertEqual(user_count,1)   # checking equal
        self.assertNotEqual(user_count,0)   # checking not equal
    
    def test_user_password(self):
        user_a = User.objects.get(username="testAdmin")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )
    

    def test_login_url(self):
        # login_url="/login/"
        # self.assertEqual(settings.LOGIN_URL,login_url)

        login_url=settings.LOGIN_URL

        # python requests - manage.py runserver
        # self.client.get , self.client.post

        # response=self.client.post(url,{},follow=True)

        data={"username":"testAdmin","password":"testAdminPassword"}
        response=self.client.post(login_url,data,
        follow=True)
        # print(dir(response))
        # print(response.request)

        status_code=response.status_code
        redirect_path=response.request.get("PATH_INFO")
        # self.assertEqual(redirect_path,settings.LOGIN_REDIRECT_URL)
        # self.assertEqual(status_code,200)
    
    def test_notes_url(self):
        
        self.client.login(username=self.user_a.username,password='testAdminPassword')
        url = reverse('notes')
        # response=self.client.get(url)
        response=self.client.post(url,{"user":self.user_a,"title":"notesTest","description":"notesTest"})
        self.assertTrue(response.status_code!=200)
        
        
        


    

# class viewTestCase(TestCase):

#     def setUp(self):

#         user_b=User.objects.create_user('testAdmin','testAdmin@gmail.com','testAdminPassword')

#         self.user_b=user_b
#         user_count=User.objects.all().count()

#         self.assertEquals(user_count,1)








    
   
