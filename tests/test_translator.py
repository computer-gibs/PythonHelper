import unittest
from translator import translate_text


class TestTranslator(unittest.TestCase):
    def test_translate_text(self):
        input_text = "Hello, world!"
        expected_output = "Здравствуй, мир!"
        translated_text = translate_text(input_text)
        self.assertEqual(translated_text, expected_output)


if __name__ == '__main__':
    unittest.main()
