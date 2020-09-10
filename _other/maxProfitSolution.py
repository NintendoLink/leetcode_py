# python 3.6.4
# encoding: utf-8
"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:

    """
    本质上是求数组中相差最大的两个数
    1、利用o(n2)算法遍历
    2、动态规划
    """
    def maxProfit(self, prices) -> int:

        profit = None
        for prev_day in range(0,len(prices)-1):
            for next_day in range(prev_day + 1,len(prices)):

                cur_profit = prices[next_day] - prices[prev_day]

                if cur_profit > 0:
                    profit = cur_profit if profit is None else\
                        max(profit,cur_profit)
        return profit if profit is not None else 0

if __name__ == '__main__':

    # arr = [7,1,5,3,6,4]
    arr = [7, 6, 4, 3, 1]
    solution = Solution()
    print(solution.maxProfit(arr))