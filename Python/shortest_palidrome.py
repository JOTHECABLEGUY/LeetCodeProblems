class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        c = f"{s}#{r}"
        kmp = [0] * len(c)
        j = 0
        for i in range(1, len(c)):
            j = kmp[i - 1]
            while j > 0 and c[i] != c[j]:
                j = kmp[j - 1]
            if c[i] == c[j]:
                j += 1
            kmp[i] = j
        return f"{r[:-kmp[-1]]}{s}"
if __name__ == "__main__":
    print(Solution().shortestPalindrome("abcd"))
    print(Solution().shortestPalindrome("aacecaaa"))