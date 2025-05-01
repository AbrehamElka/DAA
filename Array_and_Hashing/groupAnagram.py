from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashTable = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for ch in i:
                count[ord(ch) - ord("a")] += 1
            
            hashTable[tuple(count)].append(i)
        
        return hashTable.values()
        