from django.test import TestCase

# Create your tests here.
class CompliantTests(TestCase):
    def user_can_register(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def user_can_view_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
    
    