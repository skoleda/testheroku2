from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTEst(SimpleTestCase):
    def test_home_page_status_code(self):
        resource = self.client.get('/')
        self.assertEqual(resource.status_code, 200)

    def test_about_page_status_code(self):
        resource = self.client.get('/about/')
        self.assertEqual(resource.status_code, 200)