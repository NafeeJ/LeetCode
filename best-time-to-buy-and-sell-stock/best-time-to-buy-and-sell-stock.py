class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        
        for i in range(len(prices))[1:]:
            buy = buy if prices[buy] < prices[i] else i
            max_profit = max(max_profit, prices[i] - prices[buy])
            
        return max_profit