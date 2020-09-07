class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]

if __name__ == '__main__':
    s = "abccba"
    solution = Solution()
    print(solution.isPalindrome(s))