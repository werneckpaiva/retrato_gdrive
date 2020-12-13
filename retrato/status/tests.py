from django.test import TestCase

from django.test import Client


class TestHello(TestCase):

    def test_status(self):
        c = Client()
        response = c.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")

