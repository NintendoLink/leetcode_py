# python 3.6.4
# encoding: utf-8
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:

    def longestCommonPrefix(self, strs):
        """
        思路
        1、暴力解法即可
        2、利用python中字符也是数字的特性
        :param strs:
        :return:
        """

        if len(strs) == 0 or not strs:
            return ''
        res = []
        for index,ch in enumerate(strs[0]):

            for str in strs:
                if index > len(str) - 1:
                    return ''.join(res)
                if str[index] != ch:
                    return ''.join(res)
            res.append(ch)
        return ''.join(res)

if __name__ == '__main__':
    # solution = Solution()
    # # strs = ["flower","flow","flight"]
    # strs = ["aa","a"]
    # print(solution.longestCommonPrefix(strs))

    str1 = 'abc'
    str2 = 'xyz'


    pass