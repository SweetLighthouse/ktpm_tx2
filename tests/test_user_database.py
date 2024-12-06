import unittest
import mongomock
from english_learning_app.database.user_database import UserDatabase


class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        """Set up the mock database and collection before all tests."""
        self.mongo_client = mongomock.MongoClient()
        self.db = UserDatabase()
        self.db.db = self.mongo_client['english_learning_app']
        self.db.collection = self.db.db['users']
        self.db.collection.insert_many([
            {"username": "user123", "password": "pass123"},
            {"username": "john_doe", "password": "random789"},
            {"username": "tech_guru", "password": "password987"},
            {"username": "admin001", "password": "adminPass123"},
            {"username": "dev_master", "password": "codeRocks321"},
            {"username": "tester01", "password": "testMeNow567"},
            {"username": "data_hunter", "password": "dataRules890"},
            {"username": "anonymous", "password": "hiddenTruth456"},
            {"username": "superuser", "password": "superSecure789"}
        ])

    def tearDown(self):
        """Close the mock MongoDB client after all tests."""
        self.mongo_client.close()

    def test_add_user(self):
        """Test adding a new user."""
        result = self.db.add_user('testuser', 'password123')
        self.assertTrue(result, "Should return True when adding a new user.")

        cursor = self.db.collection.find({'username': 'testuser'})
        self.assertEqual(len(list(cursor)), 1, "Should return exactly one record.")

    def test_add_existing_user(self):
        """Test adding an existing user."""
        result = self.db.add_user('anonymous', 'newpassword')
        self.assertFalse(result, "Should return False when adding an existing user.")

        cursor = self.db.collection.find({'username': 'anonymous'})
        self.assertEqual(len(list(cursor)), 1, "Should return exactly one record.")

    def test_get_user(self):
        """Test retrieving a user."""
        user = self.db.get_user('user123')
        self.assertIsNotNone(user, "Should return a user.")
        self.assertEqual(user['username'], 'user123', "Should return the correct user.")

    def test_delete_user_exist(self):
        """Test deleting an existing user."""
        result = self.db.delete_user('anonymous')
        self.assertTrue(result, "Should return True for successful deletion.")

        cursor = self.db.collection.find({'username': 'anonymous'})
        self.assertEqual(len(list(cursor)), 0, "Should not find the deleted user.")

    def test_delete_user_not_exist(self):
        """Test deleting a non-existing user."""
        result = self.db.delete_user('nonexistence')
        self.assertFalse(result, "Should return False for non-existent user deletion.")

        cursor = self.db.collection.find({'username': 'nonexistence'})
        self.assertEqual(len(list(cursor)), 0, "Should not find the user.")

    def test_update_user_password(self):
        """Test updating a user's password."""
        result = self.db.update_user_password('anonymous', 'newpassword')
        self.assertTrue(result, "Should return True when password is successfully updated.")

        cursor = self.db.collection.find({'username': 'anonymous'})
        updated_user = list(cursor)[0]
        self.assertEqual(updated_user['password'], 'newpassword', "Password should be updated.")

    def test_user_exists(self):
        """Test checking if a user exists."""
        result = self.db.user_exists('dev_master')
        self.assertTrue(result, "Should return True for an existing user.")

    def test_user_not_exists(self):
        """Test checking if a user does not exist."""
        result = self.db.user_exists('nonexistence')
        self.assertFalse(result, "Should return False for a non-existing user.")

    def test_get_all_users(self):
        """Test retrieving all users."""
        users = self.db.get_all_users()
        self.assertEqual(len(users), 9, "Should return the correct number of users.")


if __name__ == '__main__':
    unittest.main()
