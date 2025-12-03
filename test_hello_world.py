import unittest
from hello_world import app, generate_html, greet


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_greet_returns_expected_message(self):
        expected = "Welcome to CI/CD 101 using GitHub Actions!"
        self.assertEqual(greet(), expected)

    def test_generate_html_wraps_message_in_html(self):
        message = "Test message"
        html = generate_html(message)
        self.assertIn(message, html)
        self.assertIn("<html>", html)
        self.assertIn("</html>", html)

    def test_greeting_route_status_code(self):
        response = self.client.get("/greeting")
        self.assertEqual(response.status_code, 200)

    def test_greeting_route_content(self):
        expected = b"Welcome to CI/CD 101 using GitHub Actions!"
        response = self.client.get("/greeting")
        self.assertIn(expected, response.data)


if __name__ == "__main__":
    unittest.main()
