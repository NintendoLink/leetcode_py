"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:

    """
    思路
    1、暴力解法
    2、KMP
    """

    def strStr(self,haystack,needle):
        # 暴力解法
        if needle is None or len(needle) == 0:
            return 0
        if haystack is None or len(haystack) == 0:
            return -1
        # 找到起始位置
        for i in range(0,len(haystack)):

            # 找到起始位置之后，遍历needle和haystack,判断每个词汇是否一致，如果不一致，重新开始
            if haystack[i] == needle[0]:
                count = 0
                for j in range(0,len(needle)):

                    # 是否已经超出下标
                    if i + j < len(haystack):
                        # 依次判断
                        if haystack[i + j] != needle[j]:
                            break
                        # 计数，如果count == len(needle)则说明对needle已经遍历结束
                        else:
                            count += 1

                    # 超出则推出此次循环
                    else:
                        break

                if count == len(needle):
                    return i
        return -1


if __name__ == '__main__':
    heystack = "hello"
    needle = "ll"

    solution = Solution()
    print(solution.strStr(haystack=heystack,needle=needle))