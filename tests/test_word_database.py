import unittest
import mongomock

from english_learning_app.database.word_database import WordDatabase

class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        """Cài đặt mock database."""
        self.mongo_client = mongomock.MongoClient() # mock server
        self.db = WordDatabase() # the dao we want to test for
        self.db.db = self.mongo_client['english_learning_app'] # mock db
        self.db.collection = self.db.db['words'] # mock collecion
        self.db.collection.insert_many([
            {"username": "john_doe", "english": "gamer", "vietnamese": "game thủ"},
            {"username": "john_doe", "english": "furthermore", "vietnamese": "hơn nữa"},
            {"username": "john_doe", "english": "kimchi", "vietnamese": "Kim chi"},
            {"username": "john_doe", "english": "anthology", "vietnamese": "Tuyển tập"},
            {"username": "john_doe", "english": "handkerchief", "vietnamese": "Khăn tay"},
            {"username": "john_doe", "english": "escapist", "vietnamese": "người chạy trốn"},
            {"username": "john_doe", "english": "ballistic", "vietnamese": "xạ kích"},
            {"username": "john_doe", "english": "convenient", "vietnamese": "tiện lợi"},
            {"username": "tester01", "english": "unremarkable", "vietnamese": "không đáng kể"},
            {"username": "tester01", "english": "remember", "vietnamese": "nhớ, nhớ lại"},
            {"username": "tester01", "english": "empty", "vietnamese": "trống rỗng"},
            {"username": "tester01", "english": "demand", "vietnamese": "yêu cầu"},
        ])
        
   
    def tearDown(self):
        """Đặt lại mỗi lần chạy test case."""
        self.mongo_client.close()
        

    def test_add_word(self):
        """Test thêm từ mới."""
        result = self.db.add_word('john_doe', 'economy', 'kinh tế')
        
        cursor = self.db.collection.find({
            "username": "john_doe",
            "english": "economy",
            "vietnamese": "kinh tế"
        })
        result_list = list(cursor)
        self.assertEqual(len(result_list), 1)
        

    def test_add_existing_word(self):
        """Test thêm từ vựng đã tồn tại."""
        result = self.db.add_word('john_doe', 'convenient', 'tiện lợi') # đã tồn tại
        self.assertFalse(result)
        
        cursor = self.db.collection.find({
            "username": "john_doe",
            "english": "convenient",
            "vietnamese": "tiện lợi"
        })
        result_list = list(cursor)
        self.assertEqual(len(result_list), 1)
        
        
    def test_get_all_words(self):
        """Test lấy danh sách từ của 1 user"""
        result = self.db.get_all_words('john_doe')
        self.assertEqual(len(result), 8)
        self.assertTrue(all(word['username'] == 'john_doe' for word in result))
        

    def test_delete_word(self):
        """Test xoá 1 từ."""
        result = self.db.delete_word('john_doe', 'handkerchief')
        self.assertTrue(result)
        cursor = self.db.collection.find({'username': 'john_doe', 'english': 'a'})
        result_list = list(cursor)
        self.assertEqual(len(result_list), 0)
        

    def test_update_word(self):
        """Test update 1 từ vựng."""
        result = self.db.update_word('john_doe', 'convenient', 'dễ chịu')
        self.assertTrue(result)
        

    def test_word_exists(self):
        """Test xem từ đã tồn tại hay không."""
        self.assertFalse(self.db.word_exists('john_doe', 'this is a made up word'))
        self.assertTrue(self.db.word_exists('john_doe', 'convenient'))
        

if __name__ == '__main__':
    unittest.main()
