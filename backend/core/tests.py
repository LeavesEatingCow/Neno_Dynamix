from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    
    def test_get(self):
        response = self.client.get(reverse("core:landing-page"))
        # Checks if status is 200, otherwise test fails
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing_page.html")