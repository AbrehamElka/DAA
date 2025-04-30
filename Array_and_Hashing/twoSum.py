class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashMap = {}
        for i, v in enumerate(nums):
            if v in hashMap:
                return [hashMap[v], i]
            hashMap[target - v] = i
        