import unittest
from translator import translate_text


class TestTranslator(unittest.TestCase):
    def test_translate_text(self):
        input_text = "My name is Sarah and I live in London"
        keywords = ["Меня зовут", "Сара", "я живу", "Лондоне"]
        translated_text = translate_text(input_text)
        for keyword in keywords:
            self.assertIn(keyword, translated_text)


if __name__ == '__main__':
    unittest.main()
