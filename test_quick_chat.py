import unittest
from quick_tools import verify_room_type
import random
import string

class QuickToolsTester(unittest.TestCase):

    def test_verify_room_type(self):

        self.assertFalse(verify_room_type("whatever"))  # Does not correspond to any of the types
        self.assertTrue(verify_room_type("public"))
        self.assertTrue(verify_room_type("private"))

    def test_verify_user_password(self):

        self.assertFalse(verify_user_password("a"))             # too short, no numbers or special char
        self.assertFalse(verify_user_password("azertyuiop"))    # no numbers or special char
        self.assertFalse(verify_user_password("azertyuiop123")) # no special char
        self.assertFalse(verify_user_password("azertyuiop!"))   # no numbers
        self.assertFalse(verify_user_password("az3!"))          # too short
        self.assertFalse(verify_user_password("az000!"))        # too short
        self.assertTrue(verify_user_password("azerty!uiop123")) # perfect
