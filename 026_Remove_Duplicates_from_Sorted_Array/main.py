class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) < 2):
            return len(nums)
        s = 0
        f = 1
        
        while (f < len(nums)):
            if (nums[s] == nums[f]):
                f += 1
            else:
                s += 1
                nums[s] = nums[f]
                f += 1
        
        return s+1
