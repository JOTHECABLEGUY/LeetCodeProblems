"""20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""
import pytest
class Solution:
    def test(self):
        return self.isValid("(){}}{")
    def isValid(self, s: str) -> bool:
        """
            Determines if the input string of parentheses is valid.

            This function checks whether the given string containing parentheses, brackets, 
            and braces is valid. A string is considered valid if every opening bracket has 
            a corresponding closing bracket in the correct order.

            Args:
                s (str): The string containing the parentheses to validate.

            Returns:
                bool: True if the string is valid, False otherwise.
        """
        
        # dictionary to map opening characters to their corresponding closing characters
        open_close_map = {'(':')',
                          '{':'}',
                          '[':']'}
        
        # list to hold the opening characters before their closers are seen in the order that they appear
        stack = []
        
        # any string that has an odd number of characters must not be valid (1 open + 1 close = 2 chars), 
        #   odd means it is certain that there are not enough closers for the openers or vice versa
        if len(s) % 2:
            return False
        
        # loop through the characters in the input string
        for char in s:
            
            # if the current char is an opener, add to the "top" of the stack
            if char in open_close_map:
                stack.append(char)
                
            # the character is not an opener,
            #   and the stack is empty or
            #   the top of the stack does not contain the current character's
            #   opener, meaning the closer came at the wrong order,
            # then the string is not valid, return False
            elif not stack or open_close_map.get(stack.pop(-1), '') != char:
                return False
        
        # return True if stack is empty (all openers found closers in the correct order),
        #   False if there are still openers on the stack (no corresponding closers found)
        return not stack
    
@pytest.mark.parametrize("s, expected", [
    # Happy path tests
    ("()", True),
    ("()[]{}", True),
    ("{[()]}", True),
    
    # Edge cases
    ("", True),
    ("(", False),
    (")", False),
    ("([)]", False),
    ("{[}", False),
    
    # Error cases
    ("{[()]", False),
    ("{[()]]", False),
    ("{[()]}{", False),
],
ids = ["single_pair", "multiple_pairs", "nested_pairs", "empty_string", "single_open_bracket", "single_close_bracket",
       "incorrectly_nested", "incomplete_nested", "missing_closing_bracket", "extra_closing_bracket", "extra_opening_bracket"])
def test_isValid(s, expected):
    # Act
    result = Solution().isValid(s)
    
    # Assert
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())