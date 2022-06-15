import math


nums = [-4,-1,0,3,10]


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared = [i*i for i in nums]
        squared.sort()
        return squared

test = Solution()
print(test.sortedSquares(nums))