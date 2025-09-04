from django.test import TestCase

# Create your tests here.
class CompliantTests(TestCase):
    def test_create_compliant(self):
        complaint = Compliant.objects.create(
            title="Test Complaint",
            description="This is a test complaint.",
            status="open"
        )
        self.assertEqual(complaint.title, "Test Complaint")
        self.assertEqual(complaint.status, "open")
        self.assertIsNotNone(complaint.created_at)
        self.assertIsNotNone(complaint.updated_at)
    
        