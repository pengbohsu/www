class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:  return 0
        d0 = 0
        d1 = - prices[0]
        
        for i in range(1,len(prices)):
            d0=max(d0,d1+prices[i])
            d1=max(d1,d0-prices[i])
        
        return d0

class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sums = 0
        for i in range(1,len(prices)):
            if (prices[i] > prices[i - 1]):
                sums += (prices[i] - prices[i - 1])
            
        return sums

    
  	
prices=[7,1,5,3,6,4]
solu=Solution1()
print(solu.maxProfit(prices))
