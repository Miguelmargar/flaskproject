import os
import unittest
from unittest import TestCase
from classifieds import *

TEST_DB = 'test.db'


class Basic_url_tests(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_howitworks_page(self):
        response = self.app.get('/howitworks', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.app.get('/create', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_contactus_page(self):
        response = self.app.get('/contactus', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
