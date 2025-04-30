class Solution(object):
    def containDuplicate(self, num):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashSet = set()

        for i in num:
            if i in hashSet:
                return True
            
            hashSet.add(i)
        
        return False