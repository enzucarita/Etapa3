from django.test import TestCase
from app.forms import CustomUserCreationForm

# Create your tests here.

class TestForms(TestCase):

    def test_custom_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'administrador',
            'first_name': 'sebastian',
            'last_name': 'fernandez',
            'email': 'sjafernandez96@gmail.com',
            'password1': 'duocduoc'
        }) 

        self.assertTrue(form.is_valid())
    
    def test_custom_user_creation_invalid_user(self):
        form = CustomUserCreationForm(data={'username': 'contador'})
        self.assertFalse(form.is_valid())
    
    def test_custom_user_creation_invalid_first_name(self):
        form = CustomUserCreationForm(data={'first_name': 'brandon'})
        self.assertFalse(form.is_valid())
    
    def test_custom_user_creation_invalid_last_name(self):
        form = CustomUserCreationForm(data={'last_name': 'jordan'})
        self.assertFalse(form.is_valid())

    def test_custom_user_creation_invalid_email(self):
        form = CustomUserCreationForm(data={'email': 'cogoteo1313#'})
        self.assertFalse(form.is_valid())

    def test_custom_user_creation_invalid_password(self):
        form = CustomUserCreationForm(data={'password1': 'malo'})
        self.assertFalse(form.is_valid())    

    def test_custom_user_creation_blankspace(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
    

