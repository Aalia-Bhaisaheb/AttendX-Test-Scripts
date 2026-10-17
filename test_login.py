import unittest

# Sample login logic for demonstration.
# This is not connected to a real AttendX application.

def login(username, password):
    if not username or not password:
        return "Username and password are required"
    if username == "student1" and password == "Pass123":
        return "Login successful"
    return "Invalid username or password"


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student1", "Pass123"),
            "Login successful"
        )

    def test_unknown_username(self):
        self.assertEqual(
            login("unknown", "Pass123"),
            "Invalid username or password"
        )


    def test_wrong_password(self):
        self.assertEqual(
            login("student1", "wrong"),
            "Invalid username or password"
        )

    def test_empty_fields(self):
        self.assertEqual(
            login("", ""),
            "Username and password are required"
        )


if __name__ == "__main__":
    unittest.main()
