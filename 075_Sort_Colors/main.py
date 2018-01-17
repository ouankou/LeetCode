class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        b = len(nums)-1
        cur = 0
        
        while (cur < len(nums) and cur <= b):
            if (nums[cur] == 0):
                nums[cur] = nums[r]
                nums[r] = 0
                cur += 1
                r += 1
            elif (nums[cur] == 2):
                nums[cur] = nums[b]
                nums[b] = 2
                b -= 1
            else:
                cur += 1
