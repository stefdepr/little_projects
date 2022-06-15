class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        index_where_it_should_be = 0
        for i in range(0, len(nums)):
            if target < nums[i]:
                index_where_it_should_be = i
            if nums[i] == target:
                print(nums[i])
                index = i
                return index
        return index_where_it_should_be
