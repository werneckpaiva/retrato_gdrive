from django.test import TestCase

from django.test import Client


class TestHello(TestCase):

    def testIsHello(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello world!")

