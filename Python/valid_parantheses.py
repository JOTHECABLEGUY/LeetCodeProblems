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
        open_close_map = {'(':')',
                          '{':'}',
                          '[':']'}
        stack = []
        if len(s) % 2:
            return False
        for char in s:
            if char in open_close_map:
                stack.append(char)
            elif not stack or open_close_map.get(stack.pop(-1), '') != char:
                return False
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