class Solution:
    """
    思路：
    1、常规方法，需要考虑特殊情况
        1）n = 0
        2) n 为2的整数幂
    """
    def binaryGap(self, n):

        res = 0
        count = 0

        # 循环到第一个1
        while(n > 0):
            if (n&1 ==0):
                n = n >> 1
            else:
                break
        # 将第一个1作为开始
        n = n >> 1

        flag= False
        while(n > 0):

            if (n & 1 == 0):
                count += 1
            else:
                res = res if res > count else count
                count = 0
                flag = True
            n = n >> 1
        return res + 1 if flag else 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.binaryGap(22))
