class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = dict()

        for i in range(0, len(nums)):
            if target - nums[i] in indices.keys():
                return [i, indices[target - nums[i]]]
            indices[nums[i]] = i