class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashMap = {}
        if len(s) != len(t):
            return False
        for i in s:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        for j in t:
            if j not in hashMap or hashMap[j] == 0:
                return False
            
            hashMap[j] -= 1
        
        return True