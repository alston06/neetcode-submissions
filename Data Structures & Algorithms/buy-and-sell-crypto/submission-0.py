class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for price in prices:
            if price < minBuy:
                minBuy = price
            profit = price - minBuy
            maxP = max(maxP, profit)
        return maxP