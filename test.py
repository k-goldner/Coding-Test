from sendjson.views import prepare_payload
import unittest
from sendjson.json_test_file import *

class TestPost(unittest.TestCase):
    def test_post_response(self):
        result = prepare_payload(json_input)
        self.assertEqual(result, json_output)

if __name__ == "__main__":
    unittest.main()


