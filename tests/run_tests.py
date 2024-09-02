import unittest
from application import app, db
from models import User

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a new test context before each test."""
        self.app = app
        self.app.config.from_object('config.TestingConfig')

        # Push an application context
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.client = self.app.test_client()

        # Create the database schema
        db.create_all()

        # Add a test user
        self.user = User(username='testuser', password='testpassword')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """Tear down the test context after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()  # Pop the application context

    def test_index(self):
        """Test the index page loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_user_login(self):
        """Test the login functionality."""
        response = self.client.post('/admin/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome, testuser", response.data)

if __name__ == '__main__':
    unittest.main()
