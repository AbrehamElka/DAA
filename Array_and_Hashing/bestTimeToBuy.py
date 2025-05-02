class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        l = 0

        for r in range(1, len(prices)):

            if (prices[r] - prices[l]) > m:
                m = prices[r] - prices[l]
            elif prices[l] > prices[r]:
                l = r
        
            
        return m
            
        