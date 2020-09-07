# python 3.6.4
# encoding: utf-8
"""

125. 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    思路
    1、常规比较做法即可
    2、天秀版本
    """
    def isPalindrome(self,s:str)-> bool:

        if s is None or len(s) < 1:
            return True

        start = 0
        end = len(s) - 1

        while(start <= end):

            # 过滤其他字符
            while(start < len(s) -1 and  not self._is_number_or_char(s[start])):
                start += 1

            while(end > -1 and not self._is_number_or_char(s[end])):
                end -= 1

            # 判断,0和P/1和Q/...的ASC码相差都为32,这里要注意判断条件
            if (start <= end):
                if not ((ord(s[start]) - ord(s[end]) == 0) or (abs(ord(s[start]) - ord(s[end])) == 32 and (ord(s[start]) > 57 and ord(s[end]) > 57))):
                    return False
                else:
                    start += 1
                    end -= 1

        return True

    def _is_number_or_char(self, char):
        assert len(char) == 1, \
            "len(char) must be equal 1"

        # asc判断是否是数字/大写字符/小写字符
        if 48 <= ord(char) <= 57 or\
            97 <= ord(char) <= 122 or \
            65 <= ord(char) <= 90:

            return True

        return False

    # 天秀版本
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]
if __name__ == '__main__':

    solution = Solution()
    # simple_str = ""
    # simple_str = "A man, a plan, a canal: Panama"
    simple_str = "race a car"
    print(solution.isPalindrome(simple_str))

    # char1 = "1"
    # char2 = "Q"
    #
    # print(ord(char1) - ord(char2))