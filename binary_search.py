list = [-1,0,3,5,9,12]
target = 2

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                print(nums[i])
                index = i
        return index

test = Solution()
print(test.search(list, target))
