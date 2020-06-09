# python 3.6.4
# encoding: utf-8
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