"""17. Letter Combinations of a Phone Number
Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9']."""
import pytest
from typing import List
from itertools import product
class Solution:
    def test(self):
        return self.letterCombinations("233")
    def letterCombinations(self, digits: str) -> List[str]:
        """
            Generates all possible letter combinations from a string of digits.

            This function takes a string of digits corresponding to a phone keypad and returns 
            all possible letter combinations that the digits can represent. It handles early exits 
            for invalid inputs and uses a mapping of digits to their respective letters to compute 
            the combinations.

            Args:
                digits (str): A string of digits (2-9) for which to generate letter combinations.

            Returns:
                List[str]: A list of all possible letter combinations that can be formed from the input digits. 
                Returns an empty list if the input is invalid or contains digits '0' or '1'.
        """
        # early exit if nothing to do
        if not digits or "0" in digits or "1" in digits:
            return []
        
        # map numbers to their phone letters
        letter_mappings = { "2": ('a','b','c'),
                            "3": ('d','e','f'),
                            "4": ('g','h','i'),
                            "5": ('j','k','l'),
                            "6": ('m','n','o'),
                            "7": ('p','q','r','s'),
                            "8": ('t','u','v'),
                            "9": ('w','x','y','z')}
        
        # compute all combinations using itertools product (need to unpack the tuples)
        mappings = product(*(letter_mappings[c] for c in digits))
        
        # create strings for each combo and return
        return ["".join(m) for m in mappings]

@pytest.mark.parametrize("digits, expected", [
    # Happy path tests
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("7", ["p", "q", "r", "s"]),
    ("", []),
    ("2", ["a", "b", "c"]),
    ("234", ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", 
             "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", 
             "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
    # Edge cases
    ("79", ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
    ("999", ["www", "wwx", "wwy", "wwz", "wxw", "wxx", "wxy", "wxz", "wyw", "wyx", "wyy", "wyz", "wzw", "wzx", "wzy", "wzz",
             "xww", "xwx", "xwy", "xwz", "xxw", "xxx", "xxy", "xxz", "xyw", "xyx", "xyy", "xyz", "xzw", "xzx", "xzy", "xzz",
             "yww", "ywx", "ywy", "ywz", "yxw", "yxx", "yxy", "yxz", "yyw", "yyx", "yyy", "yyz", "yzw", "yzx", "yzy", "yzz",
             "zww", "zwx", "zwy", "zwz", "zxw", "zxx", "zxy", "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]),
    # Error cases
    ("1", []),
    ("0", []),
    ("10", []),
    ("201", []),
], ids=[
    "happy_path_23", "happy_path_7", "empty_input", "single_digit_2", "happy_path_234",
    "edge_case_79", "edge_case_999",
    "error_case_1", "error_case_0", "error_case_10", "error_case_201"
])
def test_letter_combinations(digits, expected):
    # Act
    result = Solution().letterCombinations(digits)

    # Assert
    assert result == expected
    
if __name__ == "__main__":
    print(Solution().test())