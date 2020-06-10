# python 3.6.4
# encoding: utf-8
"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def plusOne(self, digits):
        # 思路1：普通方法
        # plusindex = len(digits)-1
        # digits[plusindex] += 1
        # bitAdd = False
        #
        # if digits[plusindex] == 10:
        #     bitAdd = True
        #     digits[plusindex] = 0
        #     plusindex -= 1
        # # bitAdd 控制是否可以结束进位 1) 已经到高位 也即是9999的情况 2)相加位没有出现10的情况
        # while(bitAdd):
        #     if plusindex == -1:
        #         break
        #     digits[plusindex] += 1
        #     if digits[plusindex] == 10:
        #         bitAdd = True
        #         digits[plusindex] = 0
        #         plusindex -= 1
        #     else:
        #         bitAdd = False
        #
        # if plusindex == -1:
        #     # 首位已经为0，999的情况
        #     digits[plusindex + 1] = 1
        #     digits.append(0)
        #     return digits
        # return digits

        # 思路2 ：利用取余运算
        for index,digit in enumerate(digits):
            digits[len(digits) - index - 1] = (digits[len(digits) - index - 1]+ 1) % 10
            if digits[len(digits) - index - 1] % 10 != 0:
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
if __name__ == '__main__':
    plusone = Solution()
    digit = [9,9,9,9]
    print(plusone.plusOne(digit))