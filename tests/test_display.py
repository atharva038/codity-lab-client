import unittest
from client.display import display_user

class DisplayTests(unittest.TestCase):
    def test_display(self):
        self.assertEqual(display_user({"fullName": "Ada"}), "Ada")
