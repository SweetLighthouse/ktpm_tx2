import unittest
from unittest.mock import patch
from english_learning_app.logic.translation_logic import translate_word


# test case cho function translate_word
# function sử dụng api từ api.mymemory.translated.net
# nên ta sẽ mock data nhận về, tức mock requests.get
def mock_requests_get(url, *args, **kwargs):
    mock_input_output_dictionary = {
        "https://api.mymemory.translated.net/get?q=hello&langpair=en|vi": {
            "status_code": 200,
            "json_data": {"responseData": {"translatedText": "xin chào"}}
        },
        "https://api.mymemory.translated.net/get?q=goodbye&langpair=en|vi": {
            "status_code": 200,
            "json_data": {"responseData": {"translatedText": "tạm biệt"}}
        },
        "https://api.mymemory.translated.net/get?q=economy&langpair=en|vi": {
            "status_code": 200,
            "json_data": {"responseData": {"translatedText": "kinh tế"}}
        },
        "https://api.mymemory.translated.net/get?q=literature&langpair=en|vi": {
            "status_code": 200,
            "json_data": {"responseData": {"translatedText": "văn học"}}
        },
        "https://api.mymemory.translated.net/get?q=century&langpair=en|vi": {
            "status_code": 200,
            "json_data": {"responseData": {"translatedText": "thế kỷ"}}
        },
        "https://api.mymemory.translated.net/get?q=@12#$%65&langpair=en|vi": {
            "status_code": 500,
            "json_data": {}
        },
    }
    if url not in mock_input_output_dictionary: return MockResponse({}, 404)  # không tìm thấy
    return MockResponse(mock_input_output_dictionary[url]["json_data"],
                        mock_input_output_dictionary[url]["status_code"])


# vĩ ta mock requests.get, mà requests.get trả về 1 object (requests.Response), nên ta cần mock luôn cả response object
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestTranslateWord(unittest.TestCase):

    @patch("requests.get", side_effect=mock_requests_get)
    def test_translate_word_status_200(self, mock_get):
        result = translate_word("hello")
        self.assertEqual(result, "xin chào", f"Expected 'xin chào', got {result}")

    @patch("requests.get", side_effect=mock_requests_get)
    def test_translate_word_non_200_status(self, mock_get):
        result = translate_word("đây là một từ chưa từng được định nghĩa")
        self.assertIsNone(result, f"Expected None, got {result}")


if __name__ == "__main__":
    unittest.main()