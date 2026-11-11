
from django.test import TestCase
from .models import Enquiry


class WebsiteTests(TestCase):

    def test_homepage_loads(self):

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)


    def test_enquiry_submission(self):

        response = self.client.post(
            "/contact/send/",
            {
                "name": "Test User",
                "email": "test@example.com",
                "phone": "9876543210",
                "service": "Film Production",
                "message": "Testing enquiry",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Enquiry.objects.count(),
            1
        )

