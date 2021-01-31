from django.test import TestCase
from .models import Registration


# Create your tests here.


class RegistrationTest(TestCase):
    def setup(self):
        d = Registration.objects.create()
        self.Username = "bhanu06"
        self.Password = "bhanu06"
        self.Email = "bhanu06@email.com"
        self.Firstname = "M"
        self.Lastname = "Bhanu"
        self.Location = "wanaparthy"
        assertEqual = (isinstance(self.Username, Registration.Username))
