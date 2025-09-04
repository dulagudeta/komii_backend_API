from django.test import TestCase

# Create your tests here.
class CompliantTests(TestCase):
    def user_can_register(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)