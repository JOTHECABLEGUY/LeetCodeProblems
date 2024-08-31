"""12. Integer to Roman
Medium
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999"""

import pytest
class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999 or num < 1:
            return ""
        factors =   [1000, 500, 100, 50, 10, 5, 1]
        roms =      ["M", "D",  "C", "L", "X", "V", "I"]
        s_array =   [""] * len(roms)
        index = 0
        while num:
            num_of_s, num = divmod(num, factors[index])
            if num_of_s == 4:
                if s_array[index-1] == roms[index-1]:
                    s_array[index-1] = f"{roms[index]}{roms[index-2]}"
                else:
                    s_array[index-1] = f"{roms[index]}{roms[index-1]}"
            elif num_of_s:
                s_array[index] = roms[index]*num_of_s
            index += 1
        return "".join(s_array)
    def test(self):
        return self.intToRoman(3888)

@pytest.mark.parametrize("num, expected", [
    (1, "I"),  # happy path
    (4, "IV"),  # edge case
    (9, "IX"),  # edge case
    (58, "LVIII"),  # happy path
    (1994, "MCMXCIV"),  # happy path
    (3888, "MMMDCCCLXXXVIII"),  # happy path
    (0, ""),  # edge case: zero
    (-1, ""),  # error case: negative number
    (4000, ""),  # error case: number too large
], ids=[
    "one", "four", "nine", "fifty-eight", "nineteen-ninety-four", "three-thousand-eight-hundred-eighty-eight",
    "zero", "negative-one", "four-thousand"
])
def test_int_to_roman(num, expected):
    # Act
    result = Solution().intToRoman(num)

    # Assert
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())