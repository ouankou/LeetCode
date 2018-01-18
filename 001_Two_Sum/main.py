class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in range (0, len(nums)):
            if (nums[i] in result):
                return [result[nums[i]], i]
            else:
                result[target-nums[i]] = i
        
        return None 
