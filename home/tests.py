from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTest(SimpleTestCase):
    def test_home_page(self):
        reponse = self.client.get('')
        print('reponse -- ', reponse)
        self.assertEquals(reponse.status_code, 200)
