"""6. Zigzag Conversion
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def test(self) -> str:
        return self.convert("PAYPALISHIRING", 6)
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        numCols = max(len(s), 1) + 1
        m = [["" for _ in range(numCols)] for _ in range(numRows)]
        column, index, s_len, num_to_add = 0, 0, len(s), numRows - 2
        while column < numCols:
            row, row_delta = 0, 1
            while row < len(m) and index < s_len:
                if column % (numRows-1):
                    row += num_to_add
                    num_to_add -= 1
                    if num_to_add <= 0:
                        num_to_add = numRows-2
                    row_delta = numRows
                m[row][column] = s[index]
                index+=1
                row += row_delta
            column += 1
        return "".join("".join(row) for row in m)
if __name__ == "__main__":
    print(Solution().test())
    print("PAHNAPLSIIGYIR", 3)
    print("PINALSIGYAHRPI", 4)