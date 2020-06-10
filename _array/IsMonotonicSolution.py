# python 3.6.4
# encoding: utf-8
"""
896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。

 

示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotonic-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    思路：普通方法判断
    """
    def isMonotonic(self, A):
        if (A is None) | (len(A) == 0):
            return False

        return self.is_increase_(A) | self.is_decrease_(A)
    def is_increase_(self,a):

        for index in range(1,len(a)):
            if a[index] < a[index-1]:
                return False
        return True
    def is_decrease_(self,a):

        for index in range(1,len(a)):
            if a[index] > a[index- 1]:
                return False
        return True

if __name__ == '__main__':
    a = [1,3,2]
    solution = Solution()
    print(solution.isMonotonic(a))