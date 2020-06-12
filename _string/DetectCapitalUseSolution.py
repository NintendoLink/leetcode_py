# python 3.6.4
# encoding: utf-8
"""
520. 检测大写字母
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-capital
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    思路：
    1、分为三种情况判断即可
    """
    def detectCapitalUse(self, word):

        if word is None or len(word) == 0:
            return False

        return self.isAllBigCase(word) or self.isAllLowCase_(word) or self.isFirstBigCase(word)
    def isAllLowCase_(self,word):

        for ch in word:
            if ord(ch) <97 or ord(ch) > 122:
                return False

        return True
    def isAllBigCase(self,word):
        for ch in word:
             if ord(ch) < 65 or ord(ch) > 90:
                 return False

        return True

    def isFirstBigCase(self,word):

        if ord(word[0]) < 65 or ord(word[0])> 90:
            return False

        for index in range(1,len(word)):
            if ord(word[index]) <97 or ord(word[index]) > 122:
                return False
        return True

if __name__ == '__main__':
    word = "alcne"
    solution = Solution()
    print(solution.DetectCapitalUseSolution(word))
