nums = [1,2,3,4,5,6,7]
k = 3



class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0 ,k):
            print(nums)
            last_number = nums[len(nums)-1]
            for i2 in range(0, len(nums)-1):
                print(nums[i2+1], nums[i2])
                nums[i2 + 1] = nums[i2]
            nums[0] = last_number


test = Solution()
test.rotate(nums, k)