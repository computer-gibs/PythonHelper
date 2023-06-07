import unittest
from main_app import generate_text


class TestMainApp(unittest.TestCase):
    def test_generate_text(self):
        input_code = "print('Hello, world!')"
        expected_output_english = "This code prints 'Hello, world!' to the console."
        result = generate_text(input_code)
        self.assertIn(expected_output_english, result[0])


if __name__ == '__main__':
    unittest.main()
