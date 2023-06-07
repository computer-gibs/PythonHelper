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
        expected_output_english = """
1. Create a class Solution and pass the string s as an argument.
2. Create the dictionary mapping the character to the top element of the mapping.
3. The code then calls the isValid method of the object and returns True if the string is valid else False.
4. Next step is to pop the stack of the current character from the stack.
5. Iterate through the string and check if the character is a mapping element.
6. For each character in the string, if it is not in the dictionary, it will return False if the char is not found.
        """
        result = generate_text(input_code)
        self.assertIn(expected_output_english, result[0])


if __name__ == '__main__':
    unittest.main()
