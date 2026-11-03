from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LogoutTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="usuario",
            password="contraseña-segura",
        )

    def test_logout_requires_post_and_redirects_to_login(self):
        self.client.force_login(self.user)

        get_response = self.client.get(reverse("logout"))
        self.assertEqual(get_response.status_code, 405)

        post_response = self.client.post(reverse("logout"))
        self.assertRedirects(post_response, reverse("login"))
        self.assertNotIn("_auth_user_id", self.client.session)
