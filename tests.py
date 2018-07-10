import os
import unittest
from unittest import TestCase
from classifieds import *

TEST_DB = 'test.db'

class BasicTests(TestCase):
    
    def setUp(self):
        self.app = app.test_client()
   
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        

if __name__ == "__main__":
    unittest.main()