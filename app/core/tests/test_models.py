from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_email_password(self):
        """ test the creation of email and password"""
        email = 'testmail@gmail.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_normailzed_email(self):
        """test for email is normalized to lower case"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'testpassword')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """test if invalid email raises validation error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'text123')

    def test_new_super_user(self):
        """test if super user created"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    


    
    
