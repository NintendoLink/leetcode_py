# python 3.6.4
# encoding: utf-8

"""
389. 找不同
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:

    """
    利用char字符求值即可
    """
    def findTheDifference(self,str1,str2):

        sum1 = sum([ord(ch) for ch in str1])
        sum2 = sum([ord(ch) for ch in str2])
        return chr(sum2 - sum1)

if __name__ == '__main__':
    str1 = "abcd"
    str2 = "abcde"

    solution = Solution()
    print(solution.findTheDifference(str1,str2))