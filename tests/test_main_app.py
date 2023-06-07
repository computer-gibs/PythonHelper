import unittest
from main_app import generate_text


class TestMainApp(unittest.TestCase):
    def test_generate_text(self):
        input_code = """
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack"""
        keywords = ["class Solution", "isValid", "stack", "mapping", "for char", "return False", "return not stack"]

        result = generate_text(input_code)
        for keyword in keywords:
            self.assertIn(keyword, result[0])


if __name__ == '__main__':
    unittest.main()
