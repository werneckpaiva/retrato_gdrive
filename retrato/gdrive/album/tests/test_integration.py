from django.test import TestCase

from django.test import Client


class TestAlbum(TestCase):

    def test_album_home(self):
        c = Client()
        response = c.get('/api/album/family')
        self.assertEqual(response.status_code, 200)
