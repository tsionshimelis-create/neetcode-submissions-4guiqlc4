class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # time to buy 
        # r time to sell
        maxP = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] >= prices[r]:
                l = r
            else:
                maxP = max(maxP, profit)

        return maxP