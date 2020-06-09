# python 3.6.4
# encoding: utf-8
"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def addBinary(self,a,b):

    #     # 思路1：
    #     # a，b分别转换为int,相加后，转将和转换为str，不过，当数很大时，不通
    #
    #     if a == "":
    #         return self.int2str(self.str2int_(b))
    #     if b == "":
    #         return self.int2str(self.str2int_(a))
    #     return self.int2str(self.str2int_(a) + self.str2int_(b))
    #
    # def str2int_(self,str):
    #
    #     if str == "":
    #         return 0
    #     jieshu = 1
    #     count = 0
    #     for index,_ in enumerate(str):
    #         count += int(str[len(str) - index -1]) * jieshu
    #         jieshu *= 2
    #     return count
    #
    # def int2str(self,number):
    #     if number == 0:
    #         return "0"
    #     res = []
    #     while number != 0:
    #         remainder = number % 2
    #         number = number // 2
    #         res.append(str(remainder))
    #     return "".join(list(reversed(res)))
        # 普通方法
        if a == "" and b == "":
            return '0'
        if a == "":
            return b
        if b == "":
            return a
        res = []
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        bitAdd = False

        for index,ch in enumerate(a):
            jw = 1 if bitAdd else 0
            sum = jw + int(a[len(a) - index - 1]) + int(b[len(a) - index - 1])
            if sum == 3:
                bitAdd = True
                res.append('1')
            elif sum == 2:
                bitAdd = True
                res.append('0')
            else:
                res.append(str(sum))
                bitAdd = False
        res = ''.join(reversed(res)) if not bitAdd else '1'+''.join(reversed(res))
        return res


if __name__ == '__main__':
    solution = Solution()
    # print(solution.int2str(53))
    # print(solution.str2int_('110101'))
    print(solution.addBinary("1010101","1"))