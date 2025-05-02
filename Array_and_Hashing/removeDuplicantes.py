class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        n = len(nums)

        for r in range(n):
            if nums[l] > nums[r]:
                break
            elif nums[l] == nums[r]:
                continue
            else:
                l += 1
                nums[l] = nums[r]

        return l + 1