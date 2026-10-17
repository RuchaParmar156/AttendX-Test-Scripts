
import unittest
from attendx_app import login


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(login("student01", "AttendX@123"))

    def test_invalid_password(self):
        self.assertFalse(login("student01", "wrongpassword"))

    def test_empty_username(self):
        self.assertFalse(login("", "AttendX@123"))

    def test_empty_password(self):
        self.assertFalse(login("student01", ""))

    def test_username_with_wrong_case(self):
        self.assertFalse(login("Student01", "AttendX@123"))


if __name__ == "__main__":
    unittest.main()
