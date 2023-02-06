from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
# TDD

User=get_user_model()

class UserTestCast(TestCase):

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
        self.assertTrue(self.user_a.check_password(self.user_a_pw))


    
   
