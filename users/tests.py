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
    
    def user_can_view_user_detail(self):
        # First, create a user to view
        response = self.client.post('/api/register/', {
            'username': 'testuser2',
            'password': 'testpassword2'
        })

    def test_user_detail(self):
        user_id = response.data['id']
        response = self.client.get(f'/api/users/{user_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser2')