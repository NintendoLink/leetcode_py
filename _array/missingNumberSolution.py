# python 3.6.4
# encoding: utf-8
"""
面试题53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

通过次数24,853提交次数55,

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:

    """
    思路1：相减法，不过没用上有序这个条件
    思路2：直接遍历
    """
    def missingNumber(self,nums):

        # # 相减法
        # length = len(nums) + 1
        # sum = length * (length - 1) / 2
        #
        # for num in nums:
        #     sum = sum - num
        #
        # return int(sum)

        # # 遍历法
        # for index in range(len(nums)):
        #     if nums[index] != index:
        #         return index
        # return len(nums)
        pass
    @staticmethod
    def binarySearch(nums,target):
        pass


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6,7,9]
    solution = Solution()
    print(solution.missingNumber(nums))
    pass