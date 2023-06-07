import unittest
from translator import translate_text


class TestTranslator(unittest.TestCase):
    def test_translate_text(self):
        input_text = "My name is Sarah and I live in London"
        expected_output = "Меня зовут Сара, и я живу в Лондоне"
        translated_text = translate_text(input_text)
        self.assertEqual(translated_text, expected_output)


if __name__ == '__main__':
    unittest.main()
